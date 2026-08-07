/**
 * fix-canonicals.js
 * Fixes canonical/og:url meta tags to use extensionless URLs,
 * and generates/updates a Netlify _redirects file to force
 * 301 redirects from *.html to the clean URL.
 *
 * Usage:
 *   node fix-canonicals.js --dry-run     (preview only, no writes)
 *   node fix-canonicals.js               (apply changes, with backups)
 */

const fs = require('fs');
const path = require('path');

const ROOT = process.cwd();
const DRY_RUN = process.argv.includes('--dry-run');
const SKIP_DIRS = new Set(['node_modules', '.git', '.netlify', 'dist', 'build', 'assets']);

let stats = {
  scanned: 0,
  canonicalFixed: 0,
  ogUrlFixed: 0,
  alreadyClean: 0,
  errors: 0,
  redirectsAdded: 0,
};

function log(msg) {
  console.log(msg);
}

function findHtmlFiles(dir, results = []) {
  let entries;
  try {
    entries = fs.readdirSync(dir, { withFileTypes: true });
  } catch (err) {
    log(`  [WARN] Could not read directory ${dir}: ${err.message}`);
    return results;
  }
  for (const entry of entries) {
    if (entry.isDirectory()) {
      if (!SKIP_DIRS.has(entry.name)) {
        findHtmlFiles(path.join(dir, entry.name), results);
      }
    } else if (entry.isFile() && entry.name.toLowerCase().endsWith('.html')) {
      results.push(path.join(dir, entry.name));
    }
  }
  return results;
}

function cleanUrl(url) {
  if (!url.toLowerCase().endsWith('.html')) return url;
  const withoutExt = url.slice(0, -5);
  if (withoutExt.endsWith('/index')) {
    return withoutExt.slice(0, -('index'.length)) || '/';
  }
  return withoutExt;
}

function fixMetaTags(content) {
  let changedCanonical = false;
  let changedOgUrl = false;

  content = content.replace(/<link\b[^>]*\brel=["']canonical["'][^>]*>/gi, (tag) => {
    const hrefMatch = tag.match(/href=["']([^"']+)["']/i);
    if (!hrefMatch) return tag;
    const original = hrefMatch[1];
    const fixed = cleanUrl(original);
    if (fixed !== original) {
      changedCanonical = true;
      return tag.replace(hrefMatch[0], `href="${fixed}"`);
    }
    return tag;
  });

  content = content.replace(/<meta\b[^>]*\bproperty=["']og:url["'][^>]*>/gi, (tag) => {
    const contentMatch = tag.match(/content=["']([^"']+)["']/i);
    if (!contentMatch) return tag;
    const original = contentMatch[1];
    const fixed = cleanUrl(original);
    if (fixed !== original) {
      changedOgUrl = true;
      return tag.replace(contentMatch[0], `content="${fixed}"`);
    }
    return tag;
  });

  return { content, changedCanonical, changedOgUrl };
}

function backupFile(filePath) {
  const backupPath = filePath + '.bak';
  if (!fs.existsSync(backupPath)) {
    fs.copyFileSync(filePath, backupPath);
  }
}

function processFile(filePath) {
  stats.scanned++;
  let original;
  try {
    original = fs.readFileSync(filePath, 'utf8');
  } catch (err) {
    log(`  [ERROR] Could not read ${filePath}: ${err.message}`);
    stats.errors++;
    return;
  }

  const { content, changedCanonical, changedOgUrl } = fixMetaTags(original);

  if (!changedCanonical && !changedOgUrl) {
    stats.alreadyClean++;
    return;
  }

  const rel = path.relative(ROOT, filePath);
  if (changedCanonical) { stats.canonicalFixed++; log(`  [canonical] ${rel}`); }
  if (changedOgUrl) { stats.ogUrlFixed++; log(`  [og:url]    ${rel}`); }

  if (DRY_RUN) return;

  try {
    backupFile(filePath);
    fs.writeFileSync(filePath, content, 'utf8');
  } catch (err) {
    log(`  [ERROR] Could not write ${filePath}: ${err.message}`);
    stats.errors++;
  }
}

function buildRedirects(htmlFiles) {
  const rootRelative = htmlFiles
    .map(f => path.relative(ROOT, f).replace(/\\/g, '/'))
    .filter(f => !f.includes('/'))
    .filter(f => f !== '404.html');

  const lines = [];
  for (const file of rootRelative) {
    const clean = cleanUrl('/' + file);
    if (clean === '/' && file === 'index.html') continue;
    if (clean !== '/' + file) {
      lines.push(`/${file}   ${clean}   301!`);
    }
  }
  return lines;
}

function writeRedirects(lines) {
  const redirectsPath = path.join(ROOT, '_redirects');
  let existing = '';
  if (fs.existsSync(redirectsPath)) {
    existing = fs.readFileSync(redirectsPath, 'utf8');
  }

  const existingLines = new Set(
    existing.split('\n').map(l => l.trim()).filter(Boolean)
  );

  const newLines = lines.filter(l => !existingLines.has(l.trim()));

  if (newLines.length === 0) {
    log('  _redirects already contains all required rules. No changes.');
    return;
  }

  stats.redirectsAdded = newLines.length;

  if (DRY_RUN) {
    log('  Would add to _redirects:');
    newLines.forEach(l => log('    ' + l));
    return;
  }

  if (fs.existsSync(redirectsPath)) {
    fs.copyFileSync(redirectsPath, redirectsPath + '.bak');
  }

  const separator = existing.trim().length > 0 ? '\n\n' : '';
  const header = existing.includes('# Canonical URL fixes')
    ? ''
    : '# Canonical URL fixes (force .html -> clean URL, added by fix-canonicals.js)\n';

  fs.appendFileSync(redirectsPath, separator + header + newLines.join('\n') + '\n');
  log(`  Wrote ${newLines.length} rule(s) to _redirects`);
}

function main() {
  log(`\nfix-canonicals.js ${DRY_RUN ? '(DRY RUN, no files will be changed)' : ''}`);
  log(`Scanning: ${ROOT}\n`);

  const htmlFiles = findHtmlFiles(ROOT);

  if (htmlFiles.length === 0) {
    log('No .html files found. Are you running this from the site root?');
    process.exit(1);
  }

  log(`Found ${htmlFiles.length} HTML file(s).\n`);
  log('--- Fixing meta tags ---');
  htmlFiles.forEach(processFile);

  log('\n--- Updating _redirects ---');
  const redirectLines = buildRedirects(htmlFiles);
  if (redirectLines.length === 0) {
    log('  No redirect rules needed.');
  } else {
    writeRedirects(redirectLines);
  }

  log('\n--- Summary ---');
  log(`Files scanned:        ${stats.scanned}`);
  log(`Canonical tags fixed: ${stats.canonicalFixed}`);
  log(`og:url tags fixed:    ${stats.ogUrlFixed}`);
  log(`Already clean:        ${stats.alreadyClean}`);
  log(`Redirect rules added: ${stats.redirectsAdded}`);
  log(`Errors:                ${stats.errors}`);

  if (stats.errors > 0) {
    log('\nCompleted with errors. Review output above before deploying.');
    process.exit(1);
  }

  if (DRY_RUN) {
    log('\nDry run complete. Re-run without --dry-run to apply changes.');
  } else {
    log('\nDone. .bak backups created for every modified file.');
    log('Review changes with: git diff');
    log('Deploy yourself with: netlify deploy --prod');
  }
}

main();
