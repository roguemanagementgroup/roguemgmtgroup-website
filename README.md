# roguemgmtgroup.com

Public web presence for **Rogue Management Group LLC**, Charlotte, NC. Systems architecture and governance firm. Home of **RogueOS**, a deterministic, locally executing autonomous agent governance framework, and the **Builder's Permit** authorization model.

Covered by USPTO provisional patent applications 63/828,137 and 63/864,057. White Paper v1.2 is published in `assets/`.

## Architecture

Static site, zero build step, zero client dependencies beyond fonts. Every page is a single self-contained HTML file with inline CSS and vanilla JS. This is deliberate: the same engineering posture the product takes, deterministic output, no framework drift, nothing executing that was not written here.

```
/
├── index.html      RogueOS: eight-primitive framework, containment guarantees, evidence posture
├── about.html      The architect: record ledger, capabilities, provenance
├── assets/         Resume, white paper, brand marks, headshots
├── sitemap.xml
├── robots.txt
├── netlify.toml    Security headers, deploy config
└── .github/
    └── workflows/
        └── build.yml   CI validation
```

## Deploy pipeline

```
VS Code edit → local commit (main) → push to GitHub → Netlify auto-deploy
```

- Pushes to `main` deploy to production. There is no staging branch by design, review happens before the push, not after.
- Security headers are enforced in `netlify.toml` (CSP, X-Frame-Options, referrer policy).
- Secrets live in the OS keyring and Netlify environment variables. Nothing sensitive is committed, ever.

## Local development

No toolchain required to view: open `index.html` in a browser. For a local server:

```powershell
npx serve .
```

## Contributing

This repository is maintained by Rogue Management Group. External pull requests are not accepted at this time. Issues for factual corrections are welcome.

## Contact

Stephen Zeitvogel, Founder and Chief Architect
stephen.zeitvogel@roguemgmtgroup.com
https://roguemgmtgroup.com

## License

See `LICENSE.txt`. Site content, RogueOS architecture, and the Builder's Permit governance model are the original work of Rogue Management Group LLC.
