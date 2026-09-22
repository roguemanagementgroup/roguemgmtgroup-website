import os
import sys
import glob

# Ensure Pillow is available for EXIF and local image processing
try:
    from PIL import Image, ImageDraw
except ImportError:
    print("[!] Pillow library is not installed on this system. Installing now...")
    import subprocess
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
        from PIL import Image, ImageDraw
        print("[+] Pillow installed and imported successfully!")
    except Exception as e:
        print(f"[!] Failed to install Pillow: {e}")
        print("[!] Please run: pip install Pillow manually.")
        sys.exit(1)
# -*- coding: utf-8 -*-
"""
Rogue Management Group - Website Compiler Script (v9 - Golden Glow & UFO Drone Update)
Author: Stephen Zeitvogel, Chief Architect | Charlotte, NC
Protected Under: The Builder's Permit Intellectual Property Governance Clause
Tag ID: Z LMK R001 | RogueOS Source Chain

This Python script is a local site builder/compiler that generates and packages the complete,
highly polished multi-page dynamic enterprise website for Rogue Management Group, LLC.
It blends the newly expanded nine page Master Architectural Blueprint directly into the web pages,
updating the embedded whitepaper viewer, dedicated governance/os pages, policy engines, and compliance mappings.

USAGE:
    1. Place this script in your local development folder (e.g., C:\\Users\\Stephen\\rogue-site).
    2. Run: python compile_rogue_site-v9.py
    3. The script will automatically create directories and write all 10 core HTML and assets files.
"""

import os

# ── DESIGN PALETTE & TYPOGRAPHY ─────────────────────────────────────────
# Carbon Background: #080B10, Foundation Dark Slate: #0F172A, Steel Borders: #1E293B
# Amber Custom: #F59E0B, Cyan Custom: #38BDF8, Emerald Custom: #10B981, Rose Custom: #EF4444, Titanium: #F8FAFC

SHARED_HEADER = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Rogue Management Group | Enterprise AI Governance and RogueOS</title>
  <meta name="description" content="Deterministic AI Governance, The Builder's Permit Authorization, and RogueOS Architecture. Founded by Stephen Zeitvogel in Charlotte, NC.">
  <meta name="author" content="Stephen Zeitvogel">

  <!-- Tailwind CSS & Lucide Icons CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://unpkg.com/lucide@latest"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            carbon: '#080B10',
            foundation: '#0F172A',
            steel: '#1E293B',
            amberCustom: '#F59E0B',
            cyanCustom: '#38BDF8',
            emeraldCustom: '#10B981',
            roseCustom: '#EF4444',
            titanium: '#F8FAFC',
          },
          fontFamily: {
            display: ['Plus Jakarta Sans', 'sans-serif'],
            mono: ['JetBrains Mono', 'monospace'],
            sans: ['Manrope', 'sans-serif'],
          }
        }
      }
    }
  </script>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Manrope:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/rm-core.css">
</head>
<body class="bg-[#080B10] text-[#F8FAFC] font-sans antialiased selection:bg-amber-500 selection:text-black">

  <!-- NAVIGATION -->
  <header class="fixed top-0 left-0 w-full z-50 bg-[#080B10]/95 backdrop-blur-md border-b border-[#1E293B]">
    <div class="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
      <a href="index.html" class="flex items-center gap-4 group">
        <!-- High Fidelity Stencil Wolf Logo -->
        <div class="relative w-12 h-12 flex items-center justify-center bg-[#0F172A]/80 border border-[#1E293B] rounded-lg group-hover:border-amber-500/50 shadow-[0_0_15px_rgba(15,23,42,0.5)] transition-all duration-300 overflow-hidden">
          <div class="absolute inset-0 bg-gradient-to-tr from-amber-500/0 via-amber-500/5 to-amber-500/0 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
          <svg class="w-10 h-10 text-slate-300 group-hover:text-amber-400 transition-all duration-300 transform group-hover:scale-105" viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <!-- Wolf Head Outline looking Right with Jagged Fur on the Left -->
            <path d="M 82 45 L 77 50 L 67 52 L 52 68 L 32 80 L 28 73 L 35 68 L 26 60 L 33 54 L 22 46 L 31 40 L 20 32 L 32 26 L 36 15 L 34 5 L 42 12 L 45 4 L 51 15 L 62 30 L 75 38 L 82 40 Z" fill="none" stroke="currentColor" />
            <!-- Stencil Cuts -->
            <path d="M 33 54 L 38 48" stroke="currentColor" stroke-width="1.5" />
            <path d="M 42 42 L 46 36" stroke="currentColor" stroke-width="1.5" />
            <!-- Glowing eye (Red Eye) -->
            <circle cx="65" cy="32" r="3" fill="#ef4444" class="animate-ping" style="animation-duration: 1.5s;" />
            <circle cx="65" cy="32" r="1.5" fill="#ef4444" />
          </svg>
        </div>
        <div>
          <span class="font-display text-lg tracking-wider uppercase font-bold text-white block leading-none">Rogue Management Group</span>
          <span class="font-mono text-[9px] text-cyan-400 uppercase tracking-widest">Charlotte, NC // Private Governance</span>
        </div>
      </a>

      <nav class="hidden lg:flex items-center gap-7 text-xs uppercase tracking-widest font-mono text-slate-300">
        <a href="implementation.html" class="hover:text-amber-400 transition-colors">Implementation</a>
        <a href="builders-permit.html" class="hover:text-amber-400 transition-colors">The Builder's Permit</a>
        <a href="rogueos.html" class="hover:text-amber-400 transition-colors">RogueOS</a>
        <a href="architect.html" class="hover:text-amber-400 transition-colors">The Architect</a>
        <a href="index.html#whitepaper" class="hover:text-cyan-400 transition-colors flex items-center gap-1">
          <span class="w-2 h-2 rounded-full bg-cyan-400 animate-pulse"></span> Thesis
        </a>
        <div class="relative group/menu">
          <button class="hover:text-amber-400 transition-colors flex items-center gap-1">More <i data-lucide="chevron-down" class="w-3 h-3"></i></button>
          <div class="absolute right-0 top-full mt-2 w-48 bg-[#0F172A] border border-[#1E293B] shadow-xl rounded-md py-2 hidden group-hover/menu:block">
            <a href="framework.html" class="block px-4 py-2 hover:bg-[#1E293B] transition-colors text-slate-300 hover:text-white">Framework Specs</a>
            <a href="evidence.html" class="block px-4 py-2 hover:bg-[#1E293B] transition-colors text-slate-300 hover:text-white">Evidence Ledger</a>
            <a href="glossary.html" class="block px-4 py-2 hover:bg-[#1E293B] transition-colors text-slate-300 hover:text-white">Lexicon</a>
            <a href="trades.html" class="block px-4 py-2 hover:bg-[#1E293B] transition-colors text-slate-300 hover:text-white">American Build</a>
            <a href="contact.html" class="block px-4 py-2 hover:bg-[#1E293B] transition-colors text-slate-300 hover:text-white">Contact HQ</a>
          </div>
        </div>
      </nav>

      <div class="flex items-center gap-4">
        <a href="contact.html" class="hidden sm:inline-block bg-amber-500 hover:bg-amber-400 text-black font-mono text-xs font-bold uppercase tracking-wider px-5 py-2.5 transition-all shadow-[0_0_20px_rgba(245,158,11,0.3)]">Open The Channel</a>
        <button class="lg:hidden text-white hover:text-amber-400 focus:outline-none" id="mobile-menu-btn">
          <i data-lucide="menu" class="w-6 h-6"></i>
        </button>
      </div>
    </div>
  </header>

  <!-- MOBILE MENU DRAWER -->
  <div class="fixed inset-0 z-40 bg-[#080B10]/95 backdrop-blur-md border-b border-[#1E293B] hidden pt-24 px-6 flex-col gap-6" id="mobile-menu">
    <nav class="flex flex-col gap-5 text-sm uppercase tracking-widest font-mono text-slate-300">
      <a href="implementation.html" class="hover:text-amber-400 transition-colors py-2 border-b border-slate-800">01 // Implementation</a>
      <a href="builders-permit.html" class="hover:text-amber-400 transition-colors py-2 border-b border-slate-800">02 // The Builder's Permit</a>
      <a href="rogueos.html" class="hover:text-amber-400 transition-colors py-2 border-b border-slate-800">03 // RogueOS</a>
      <a href="architect.html" class="hover:text-amber-400 transition-colors py-2 border-b border-slate-800">04 // The Architect</a>
      <a href="index.html#whitepaper" class="hover:text-cyan-400 transition-colors py-2 border-b border-slate-800">05 // Thesis</a>
      <a href="framework.html" class="hover:text-amber-400 transition-colors py-2 border-b border-slate-800">06 // Framework Specs</a>
      <a href="evidence.html" class="hover:text-amber-400 transition-colors py-2 border-b border-slate-800">07 // Evidence Ledger</a>
      <a href="glossary.html" class="hover:text-amber-400 transition-colors py-2 border-b border-slate-800">08 // Lexicon</a>
      <a href="trades.html" class="hover:text-amber-400 transition-colors py-2 border-b border-slate-800">09 // American Build</a>
      <a href="contact.html" class="hover:text-amber-400 transition-colors py-2 border-b border-slate-800">10 // Contact HQ</a>
    </nav>
  </div>
"""

SHARED_FOOTER = """
  <!-- CONTACT CTA -->
  <section class="py-24 bg-black border-t border-[#1E293B]">
    <div class="max-w-4xl mx-auto px-6 text-center reveal">
      <h2 class="text-3xl sm:text-5xl font-display font-black uppercase text-white tracking-tight mb-6">
        Build the system. Govern the autonomy. Keep the human in the loop.
      </h2>
      <p class="text-slate-400 text-base sm:text-lg mb-10">
        If you need an AI compliance and security audit for your Charlotte based company or want to license our code, open the channel today.
      </p>
      <a href="mailto:stephen.zeitvogel@roguemgmtgroup.com" class="bg-amber-500 hover:bg-amber-400 text-black font-mono text-xs font-bold uppercase tracking-wider px-8 py-4 inline-block shadow-[0_0_25px_rgba(245,158,11,0.4)] transition-all">stephen.zeitvogel@roguemgmtgroup.com</a>
    </div>
  </section>

  <footer class="bg-[#080B10] border-t border-[#1E293B] py-16 text-slate-500 font-mono text-xs text-center">
    <p class="text-white font-bold uppercase mb-2">Rogue Management Group, LLC</p>
    <p class="text-slate-400">Charlotte, North Carolina // All Rights Reserved © 2026</p>
    
    <!-- SOCIAL FEEDS & CHANNELS -->
    <div class="flex items-center justify-center gap-6 mt-6">
      <a href="https://youtube.com/@jackiediesel" target="_blank" class="text-slate-500 hover:text-amber-500 transition-colors flex items-center gap-1.5" title="YouTube Channel">
        <i data-lucide="youtube" class="w-4 h-4"></i> YouTube
      </a>
      <a href="https://linkedin.com/in/stephenzeitvogel" target="_blank" class="text-slate-500 hover:text-cyan-400 transition-colors flex items-center gap-1.5" title="LinkedIn Professional Network">
        <i data-lucide="linkedin" class="w-4 h-4"></i> LinkedIn
      </a>
      <a href="https://github.com/roguemanagementgroup" target="_blank" class="text-slate-500 hover:text-emerald-400 transition-colors flex items-center gap-1.5" title="GitHub Repositories">
        <i data-lucide="github" class="w-4 h-4"></i> GitHub
      </a>
      <a href="https://soundcloud.com/jackiediesel" target="_blank" class="text-slate-500 hover:text-rose-400 transition-colors flex items-center gap-1.5" title="SoundCloud Music Profile">
        <i data-lucide="music" class="w-4 h-4"></i> SoundCloud
      </a>
    </div>
  </footer>

  <!-- CORE SCRIPTS -->
  <script src="assets/js/rm-app.js"></script>
</body>
</html>
"""

# ── PAGES DEFINITIONS ───────────────────────────────────────────────────

INDEX_HTML_CONTENT = """
  <main>
    <!-- 01: HERO SECTION -->
    <section class="relative min-h-[92vh] flex items-center justify-center pt-20 overflow-hidden bg-black">
      <canvas id="construction-canvas"></canvas>
      <div class="absolute inset-0 z-0">
        <img src="assets/img/hero-construction.jpg" alt="Active Heavy Infrastructure" class="w-full h-full object-cover opacity-25 filter contrast-125 brightness-75">
        <div class="absolute inset-0 bg-gradient-to-t from-[#080B10] via-[#080B10]/70 to-transparent"></div>
        <div class="absolute inset-0 bg-gradient-to-r from-[#080B10] via-transparent to-[#080B10]"></div>
      </div>

      <div class="relative z-10 max-w-5xl mx-auto px-6 py-20 text-center">
        <div class="inline-flex items-center gap-2 px-4 py-1.5 bg-amber-500/10 border border-amber-500/30 text-amber-400 font-mono text-xs uppercase tracking-widest mb-8 glow-amber">
          <span class="w-2.5 h-2.5 rounded-full bg-amber-500 animate-ping"></span>
          Standard 00 // Autonomous Governance Reference Architecture
        </div>

        <h1 class="text-4xl sm:text-6xl md:text-7xl font-display font-black tracking-tight text-white uppercase leading-[1.05] mb-6">
          The Largest Construction Project In Fifty Years <span class="text-transparent bg-clip-text bg-gradient-to-r from-amber-400 to-amber-500">Needs A Permit.</span>
        </h1>

        <p class="text-xl sm:text-2xl font-mono text-cyan-400 font-bold mb-8 tracking-wide uppercase">We Built It.</p>

        <p class="max-w-3xl mx-auto text-base sm:text-lg text-slate-300 mb-12 font-normal leading-relaxed">
          AI is no longer just typing text, it is running code and making decisions. Rogue Management Group builds the guardrails that keep these systems in their lane.
        </p>

        <div class="flex flex-col sm:flex-row items-center justify-center gap-5">
          <a href="contact.html" class="w-full sm:w-auto bg-amber-500 hover:bg-amber-400 text-black font-mono text-xs font-bold uppercase tracking-wider px-8 py-4 transition-all shadow-[0_0_25px_rgba(245,158,11,0.35)]">Request An AI Risk & Workflow Audit</a>
          <a href="#whitepaper" class="w-full sm:w-auto bg-[#0F172A] hover:bg-slate-800 text-white font-mono text-xs font-semibold uppercase tracking-wider px-8 py-4 border border-cyan-500/40 glow-cyan transition-all flex items-center justify-center gap-2">Read The Master Thesis →</a>
        </div>
      </div>
    </section>

    <!-- 02: TERMINAL FEED -->
    <section class="py-12 bg-black border-y border-[#1E293B]">
      <div class="max-w-7xl mx-auto px-6">
        <div class="bg-[#080B10] border border-[#1E293B] p-6 font-mono text-xs shadow-2xl relative overflow-hidden">
          <div class="flex items-center justify-between border-b border-[#1E293B] pb-4 mb-4 text-slate-400">
            <div class="flex items-center gap-2">
              <span class="w-3 h-3 rounded-full bg-emerald-500"></span>
              <span class="text-white font-bold uppercase">RogueOS // DETERMINISTIC EXECUTION LOG</span>
            </div>
            <span class="text-cyan-400">STATE: MUTATION_GUARD_ACTIVE</span>
          </div>
          <div class="space-y-2 text-slate-300" id="terminal-feed">
            <p><span class="text-slate-500">></span> sys_verify: Checking local multisig authority keys... <span class="text-emerald-400">[VALIDATED]</span></p>
            <p><span class="text-slate-500">></span> consensus_arbiter: 3/3 local models reached mathematical agreement.</p>
            <p><span class="text-slate-500">></span> sha256_hash: f6590bc39e1f8d4c... <span class="text-amber-400">[IMMUTABLE WAL RECORD LOCKED]</span></p>
          </div>
        </div>
      </div>
    </section>

    <!-- 03: EIGHT STAGE DETERMINISTIC RUNTIME LIFECYCLE (WITH SCROLL REVEAL) -->
    <section id="lifecycle" class="py-28 bg-[#080B10]">
      <div class="max-w-7xl mx-auto px-6">
        <div class="text-center max-w-3xl mx-auto mb-20 reveal">
          <p class="font-mono text-xs text-amber-500 uppercase tracking-widest mb-3">Architectural Standard</p>
          <h2 class="text-3xl sm:text-4xl font-display font-bold uppercase tracking-tight text-white">The Eight Stage Deterministic Lifecycle</h2>
          <p class="text-slate-400 mt-4">We separate probabilistic model outputs from governed execution. The agent can plan, but every physical tool action must pass our strict sequence of runtime enforcements.</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-4 gap-6">
          <!-- Stage 1 -->
          <div class="bg-[#0F172A] border border-[#1E293B] p-6 relative group hover:border-amber-500/60 transition-all reveal glow-amber">
            <span class="font-mono text-xs font-bold text-amber-400 block mb-2">STAGE 01</span>
            <h3 class="text-lg font-display font-bold text-white uppercase mb-2">Initialization</h3>
            <p class="text-xs text-slate-300 leading-relaxed">Fix the system state and environment variables before any action occurs.</p>
          </div>

          <!-- Stage 2 -->
          <div class="bg-[#0F172A] border border-[#1E293B] p-6 relative group hover:border-amber-500/60 transition-all reveal">
            <span class="font-mono text-xs font-bold text-amber-400 block mb-2">STAGE 02</span>
            <h3 class="text-lg font-display font-bold text-white uppercase mb-2">Policy Gate</h3>
            <p class="text-xs text-slate-300 leading-relaxed">Check permissions and limits using open policy agent logic.</p>
          </div>

          <!-- Stage 3 -->
          <div class="bg-[#0F172A] border border-[#1E293B] p-6 relative group hover:border-amber-500/60 transition-all reveal">
            <span class="font-mono text-xs font-bold text-amber-400 block mb-2">STAGE 03</span>
            <h3 class="text-lg font-display font-bold text-white uppercase mb-2">Validation</h3>
            <p class="text-xs text-slate-300 leading-relaxed">Evaluate input parameters under a strict deny by default ruleset.</p>
          </div>

          <!-- Stage 4 -->
          <div class="bg-[#0F172A] border border-[#1E293B] p-6 relative group hover:border-amber-500/60 transition-all reveal">
            <span class="font-mono text-xs font-bold text-amber-400 block mb-2">STAGE 04</span>
            <h3 class="text-lg font-display font-bold text-white uppercase mb-2">Execution</h3>
            <p class="text-xs text-slate-300 leading-relaxed">Run code inside isolated container enclaves with network access cut off.</p>
          </div>

          <!-- Stage 5 -->
          <div class="bg-[#0F172A] border border-[#1E293B] p-6 relative group hover:border-cyan-500/60 transition-all reveal">
            <span class="font-mono text-xs font-bold text-cyan-400 block mb-2">STAGE 05</span>
            <h3 class="text-lg font-display font-bold text-white uppercase mb-2">Recovery</h3>
            <p class="text-xs text-slate-300 leading-relaxed">Catch execution anomalies and manage errors to prevent runaway loops.</p>
          </div>

          <!-- Stage 6 -->
          <div class="bg-[#0F172A] border border-[#1E293B] p-6 relative group hover:border-cyan-500/60 transition-all reveal">
            <span class="font-mono text-xs font-bold text-cyan-400 block mb-2">STAGE 06</span>
            <h3 class="text-lg font-display font-bold text-white uppercase mb-2">Continuity</h3>
            <p class="text-xs text-slate-300 leading-relaxed">Write permanent records of intent and actions to local databases.</p>
          </div>

          <!-- Stage 7 -->
          <div class="bg-[#0F172A] border border-[#1E293B] p-6 relative group hover:border-cyan-500/60 transition-all reveal">
            <span class="font-mono text-xs font-bold text-cyan-400 block mb-2">STAGE 07</span>
            <h3 class="text-lg font-display font-bold text-white uppercase mb-2">Compliance</h3>
            <p class="text-xs text-slate-300 leading-relaxed">Map execution metrics directly to standard nist and soc security controls.</p>
          </div>

          <!-- Stage 8 -->
          <div class="bg-[#0F172A] border border-[#1E293B] p-6 relative group hover:border-cyan-500/60 transition-all reveal glow-cyan">
            <span class="font-mono text-xs font-bold text-cyan-400 block mb-2">STAGE 08</span>
            <h3 class="text-lg font-display font-bold text-white uppercase mb-2">Verification</h3>
            <p class="text-xs text-slate-300 leading-relaxed">Replay execution paths to confirm compliance without sharing private weights.</p>
          </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mt-16">
          <div class="bg-[#0F172A] border border-[#1E293B] p-8 relative group hover:border-amber-500/60 transition-all reveal glow-amber">
            <div class="flex items-center justify-between mb-6">
              <span class="font-mono text-xs font-bold text-amber-400 px-2.5 py-1 bg-amber-400/10 border border-amber-400/20">LEVEL 01</span>
              <span class="text-xs font-mono text-slate-500">COMMERCIAL</span>
            </div>
            <h3 class="text-2xl font-display font-bold text-white uppercase mb-4">Implementation</h3>
            <p class="text-sm text-slate-300 mb-6 leading-relaxed">How organizations put AI to work. End to end CRM/API routing, agent integration, and workflow automation.</p>
            <a href="implementation.html" class="text-xs font-mono text-amber-400 hover:text-white uppercase tracking-wider flex items-center gap-1">Explore Services →</a>
          </div>

          <div class="bg-[#0F172A] border border-[#1E293B] p-8 relative group hover:border-emerald-500/60 transition-all reveal">
            <div class="flex items-center justify-between mb-6">
              <span class="font-mono text-xs font-bold text-emerald-400 px-2.5 py-1 bg-emerald-400/10 border border-emerald-400/20">LEVEL 02</span>
              <span class="text-xs font-mono text-slate-500">CONTROL</span>
            </div>
            <h3 class="text-2xl font-display font-bold text-white mb-4">The Builder's Permit</h3>
            <p class="text-sm text-slate-300 mb-6 leading-relaxed">How organizations control AI agency. Evaluates operational authority, constraints, and intent on demand.</p>
            <a href="builders-permit.html" class="text-xs font-mono text-emerald-400 hover:text-white uppercase tracking-wider flex items-center gap-1">Explore Permit Kernel →</a>
          </div>

          <div class="bg-[#0F172A] border border-[#1E293B] p-8 relative group hover:border-cyan-500/60 transition-all reveal glow-cyan">
            <div class="flex items-center justify-between mb-6">
              <span class="font-mono text-xs font-bold text-cyan-400 px-2.5 py-1 bg-cyan-400/10 border border-cyan-400/20">LEVEL 03</span>
              <span class="text-xs font-mono text-slate-500">RESEARCH</span>
            </div>
            <h3 class="text-2xl font-display font-bold text-white mb-4">RogueOS</h3>
            <p class="text-sm text-slate-300 mb-6 leading-relaxed">The modular offline architecture. Local enclaves, trust based scheduling, and immutable ledgers.</p>
            <a href="rogueos.html" class="text-xs font-mono text-cyan-400 hover:text-white uppercase tracking-wider flex items-center gap-1">Explore RogueOS Architecture →</a>
          </div>
        </div>
      </div>
    </section>

    <!-- 05: EMBEDDED MASTER THESIS & BLUEPRINT VIEWER -->
    <section id="whitepaper" class="py-28 bg-[#080B10] border-t border-[#1E293B]">
      <div class="max-w-7xl mx-auto px-6">
        <div class="text-center max-w-3xl mx-auto mb-12 reveal">
          <span class="font-mono text-xs font-bold text-cyan-400 px-3 py-1 bg-cyan-400/10 border border-cyan-400/20 uppercase">Master Thesis Publication</span>
          <h2 class="text-3xl sm:text-5xl font-display font-black uppercase text-white mt-4">Master Architectural Specification</h2>
          <p class="text-slate-400 mt-4 font-mono text-xs">RogueOS v2.0 • Z LMK R001 Engine • USPTO Provisional Ref 63/864,057</p>
        </div>

        <!-- Embedded Interactive Thesis Reader -->
        <div class="border-2 border-[#1E293B] bg-[#0F172A] shadow-2xl overflow-hidden reveal">
          <div class="bg-[#1E293B] p-4 flex flex-wrap items-center justify-between gap-4 border-b border-slate-700">
            <div class="flex items-center gap-3">
              <span class="w-3 h-3 rounded-full bg-cyan-400 animate-pulse"></span>
              <span class="font-mono text-xs font-bold text-white uppercase">INTERACTIVE VIEWPORT: Rogue_Master_Architectural_Blueprint.pdf</span>
            </div>
            <div class="flex items-center gap-3">
              <a href="Rogue_Master_Architectural_Blueprint.pdf" target="_blank" class="bg-amber-500 hover:bg-amber-400 text-black font-mono text-xs font-bold uppercase px-4 py-2 transition-all">Download Thesis PDF ↗</a>
            </div>
          </div>

          <!-- Tab Bar Navigation for Chapters -->
          <div class="bg-[#080B10] border-b border-[#1E293B] flex overflow-x-auto text-xs font-mono uppercase tracking-wider">
            <button id="btn-ch1" onclick="switchTab('ch1')" class="tab-btn px-6 py-4 border-b-2 border-amber-500 text-amber-400 font-bold whitespace-nowrap">CH I: System Core</button>
            <button id="btn-ch2" onclick="switchTab('ch2')" class="tab-btn px-6 py-4 border-b-2 border-transparent text-slate-400 hover:text-white whitespace-nowrap">CH II: Paradigm & Domains</button>
            <button id="btn-ch3" onclick="switchTab('ch3')" class="tab-btn px-6 py-4 border-b-2 border-transparent text-slate-400 hover:text-white whitespace-nowrap">CH III: Permit Kernel</button>
            <button id="btn-ch4" onclick="switchTab('ch4')" class="tab-btn px-6 py-4 border-b-2 border-transparent text-slate-400 hover:text-white whitespace-nowrap">CH IV: Subsystems & Fleet</button>
            <button id="btn-exhibits" onclick="switchTab('exhibits') class="tab-btn px-6 py-4 border-b-2 border-transparent text-slate-400 hover:text-white whitespace-nowrap">Exhibits: Competitive Matrix</button>
            <button id="btn-appendix" onclick="switchTab('appendix')" class="tab-btn px-6 py-4 border-b-2 border-transparent text-slate-400 hover:text-white whitespace-nowrap">Appendix: Code & Compliance</button>
          </div>

          <div class="p-8 sm:p-12 space-y-12 max-h-[800px] overflow-y-auto font-sans text-sm text-slate-300 leading-relaxed">

            <!-- Panel 1: Chapter I -->
            <div id="panel-ch1" class="whitepaper-panel space-y-6">
              <div class="border-l-4 border-amber-500 pl-4 py-1">
                <span class="font-mono text-xs text-amber-500 block uppercase">Chapter I</span>
                <h3 class="text-2xl font-display font-bold text-white uppercase font-black">Executive Summary & System Core</h3>
              </div>
              <p>Rogue Management Group (RMG) is a Charlotte based full stack software development and architectural firm that specializes in autonomous artificial intelligence engineering. The core objective of RMG is to build highly secure, auditable, and non runaway autonomous computing environments.</p>
              <p>As frontier foundation models grow in cognitive capability, they are increasingly given the operational authority to execute complex workflows. This introduces a critical industrial vulnerability, autonomy without deterministic governance.</p>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-6 bg-[#080B10] p-6 border border-[#1E293B]">
                <div>
                  <h4 class="font-display font-bold text-white uppercase text-base mb-2">The Industrial Risk</h4>
                  <p class="text-xs text-slate-400">Existing security systems authorize identities but do not evaluate the operational intent of autonomous agents throughout execution.</p>
                </div>
                <div>
                  <h4 class="font-display font-bold text-cyan-400 uppercase text-base mb-2">The Modular Solution</h4>
                  <p class="text-xs text-slate-400">RogueOS integrates governance directly into runtime behavior. No execution occurs without explicit, cryptographically verifiable, intent bounded authority.</p>
                </div>
              </div>
            </div>

            <!-- Panel 2: Chapter II -->
            <div id="panel-ch2" class="whitepaper-panel hidden space-y-6">
              <div class="border-l-4 border-amber-500 pl-4 py-1">
                <span class="font-mono text-xs text-amber-500 block uppercase">Chapter II</span>
                <h3 class="text-2xl font-display font-bold text-white font-black">The RogueOS Paradigm & Architectural Domains</h3>
              </div>
              <p>RogueOS proposes an operating system paradigm shift from resource centric scheduling to authority centric execution. It schedules agency itself, evaluating active trust scores to control permissions dynamically.</p>
              <h4 class="font-display font-bold text-white text-lg">The 5 Logical Domains of RogueOS</h4>
              <div class="grid grid-cols-1 sm:grid-cols-5 gap-4">
                <div class="bg-[#080B10] border border-[#1E293B] p-4 rounded text-center">
                  <span class="text-amber-500 block font-mono font-bold mb-1">01</span>
                  <p class="text-xs font-bold text-white">GOVERNANCE</p>
                </div>
                <div class="bg-[#080B10] border border-[#1E293B] p-4 rounded text-center">
                  <span class="text-amber-500 block font-mono font-bold mb-1">02</span>
                  <p class="text-xs font-bold text-white">EXECUTION</p>
                </div>
                <div class="bg-[#080B10] border border-[#1E293B] p-4 rounded text-center">
                  <span class="text-amber-500 block font-mono font-bold mb-1">03</span>
                  <p class="text-xs font-bold text-white">EVIDENCE</p>
                </div>
                <div class="bg-[#080B10] border border-[#1E293B] p-4 rounded text-center">
                  <span class="text-amber-500 block font-mono font-bold mb-1">04</span>
                  <p class="text-xs font-bold text-white">SECURITY</p>
                </div>
                <div class="bg-[#080B10] border border-[#1E293B] p-4 rounded text-center">
                  <span class="text-amber-500 block font-mono font-bold mb-1">05</span>
                  <p class="text-xs font-bold text-white">INTEGRATION</p>
                </div>
              </div>
            </div>

            <!-- Panel 3: Chapter III -->
            <div id="panel-ch3" class="whitepaper-panel hidden space-y-6">
              <div class="border-l-4 border-amber-500 pl-4 py-1">
                <span class="font-mono text-xs text-amber-500 block uppercase">Chapter III</span>
                <h3 class="text-2xl font-display font-bold text-white font-black">The Builder's Permit Kernel & Risk Tiers</h3>
              </div>
              <p>Every privileged action requires an associated cryptographic permit containing 10 critical metadata fields including UUID, Request Origin, Operational Intent, Temporal Duration, Resource Constraints, and Signature Seals.</p>
              <h4 class="font-display font-bold text-white uppercase text-lg">The 5 Risk Tiers of Autonomous Operations</h4>
              <div class="space-y-3 font-mono text-xs">
                <div class="p-3 bg-[#080B10] border border-slate-800 flex justify-between items-center">
                  <span class="text-emerald-400 font-bold">LEVEL 1 // MINIMAL IMPACT</span>
                  <span class="text-slate-400">Routine reading, processing information, local only</span>
                </div>
                <div class="p-3 bg-[#080B10] border border-slate-800 flex justify-between items-center">
                  <span class="text-emerald-500 font-bold">LEVEL 2 // MODERATE SIGNIFICANCE</span>
                  <span class="text-slate-400">Controlled infrastructure interactions, database reads</span>
                </div>
                <div class="p-3 bg-[#080B10] border border-slate-800 flex justify-between items-center">
                  <span class="text-amber-400 font-bold">LEVEL 3 // ENTERPRISE IMPACT</span>
                  <span class="text-slate-400">Administrative writes, sensitive database access</span>
                </div>
                <div class="p-3 bg-[#080B10] border border-slate-800 flex justify-between items-center">
                  <span class="text-amber-500 font-bold">LEVEL 4 // CRITICAL INFRASTRUCTURE</span>
                  <span class="text-slate-400">Production environment modifications, deployment, IAM keys</span>
                </div>
                <div class="p-3 bg-[#080B10] border border-slate-800 flex justify-between items-center">
                  <span class="text-rose-500 font-bold animate-pulse">LEVEL 5 // MISSION CRITICAL</span>
                  <span class="text-slate-400">National security, medical devices, safety critical actions</span>
                </div>
              </div>
            </div>

            <!-- Panel 4: Chapter IV -->
            <div id="panel-ch4" class="whitepaper-panel hidden space-y-6">
              <div class="border-l-4 border-amber-500 pl-4 py-1">
                <span class="font-mono text-xs text-amber-500 block uppercase">Chapter IV</span>
                <h3 class="text-2xl font-display font-bold text-white uppercase font-black">Active Governance Subsystems & Fleet Identity</h3>
              </div>
              <p>RogueOS secures enterprise systems through three synchronized core subsystems: the Governance Engine, the Evidence Ledger / Flight Data Recorder, and the calculated Trust Fabric.</p>
              <div class="p-5 bg-[#080B10] border border-[#1E293B]">
                <h4 class="font-display font-bold text-white uppercase text-base mb-2">Fleet Aviation Analogy</h4>
                <p class="text-xs text-slate-400 leading-relaxed font-mono">Just like commercial airlines identify and track thousands of aircraft across distinct airspaces, RogueOS implements a unique persistent cryptographic Fleet Tail Number scheme for every autonomous agent.</p>
              </div>
            </div>

            <!-- Panel 5: Exhibits -->
            <div id="panel-exhibits" class="whitepaper-panel hidden space-y-6">
              <div class="border-l-4 border-amber-500 pl-4 py-1">
                <span class="font-mono text-xs text-amber-500 block uppercase">Exhibit A</span>
                <h3 class="text-2xl font-display font-bold text-white uppercase font-black">The Comparative Governance Matrix</h3>
              </div>
              <div class="overflow-x-auto">
                <table class="w-full text-left font-mono text-xs border-collapse">
                  <thead>
                    <tr class="bg-[#080B10] border-b border-slate-700 text-slate-400 uppercase tracking-wider">
                      <th class="p-3">Control Lifecycle Phase</th>
                      <th class="p-3">LangGraph</th>
                      <th class="p-3">Temporal</th>
                      <th class="p-3">OPA</th>
                      <th class="p-3">AWS Guardrails</th>
                      <th class="p-3 text-amber-400">RogueOS (RMG)</th>
                    </tr>
                  </thead>
                  <tbody class="divide-y divide-[#1E293B] bg-[#0F172A]">
                    <tr>
                      <td class="p-3 font-bold text-slate-300">Policy Gate (A)</td>
                      <td class="p-3 text-slate-500">Manual / custom code</td>
                      <td class="p-3 text-slate-500">N/A (Workflows)</td>
                      <td class="p-3 text-emerald-400">Yes (Rego engine)</td>
                      <td class="p-3 text-emerald-400">Yes (Cloud rules)</td>
                      <td class="p-3 text-emerald-400 font-bold">Yes (Declarative Rego)</td>
                    </tr>
                    <tr>
                      <td class="p-3 font-bold text-slate-300">Provenance Log (B)</td>
                      <td class="p-3 text-emerald-400">Through LangSmith</td>
                      <td class="p-3 text-slate-500">Telemetry only</td>
                      <td class="p-3 text-slate-500">N/A</td>
                      <td class="p-3 text-slate-400">AWS CloudTrail</td>
                      <td class="p-3 text-emerald-400 font-bold">Yes (OTel + Langfuse)</td>
                    </tr>
                    <tr>
                      <td class="p-3 font-bold text-slate-300">Checkpointing (C)</td>
                      <td class="p-3 text-emerald-400">Yes (State DB)</td>
                      <td class="p-3 text-emerald-400">Yes (Event sourcing)</td>
                      <td class="p-3 text-slate-500">N/A</td>
                      <td class="p-3 text-slate-500">N/A</td>
                      <td class="p-3 text-emerald-400 font-bold">Yes (SQLite state)</td>
                    </tr>
                    <tr>
                      <td class="p-3 font-bold text-slate-300">Agent Registry (D)</td>
                      <td class="p-3 text-slate-500">N/A</td>
                      <td class="p-3 text-emerald-400">Yes (Namespaces)</td>
                      <td class="p-3 text-slate-500">N/A</td>
                      <td class="p-3 text-slate-500">N/A</td>
                      <td class="p-3 text-emerald-400 font-bold">Yes (Private enclaves)</td>
                    </tr>
                    <tr>
                      <td class="p-3 font-bold text-slate-300">Detain/Quarantine (E)</td>
                      <td class="p-3 text-rose-500">No (Exception)</td>
                      <td class="p-3 text-rose-500">No (Retry loop)</td>
                      <td class="p-3 text-rose-500">No (Hard deny)</td>
                      <td class="p-3 text-rose-500">No (Hard block)</td>
                      <td class="p-3 text-emerald-400 font-bold">Yes (Holding + review)</td>
                    </tr>
                    <tr>
                      <td class="p-3 font-bold text-slate-300">Local Security (F)</td>
                      <td class="p-3 text-rose-500">No (Cloud tethered)</td>
                      <td class="p-3 text-slate-400">Self hostable</td>
                      <td class="p-3 text-emerald-400">Yes</td>
                      <td class="p-3 text-rose-500">No (Cloud locked)</td>
                      <td class="p-3 text-emerald-400 font-bold">Yes (Air gapped local build)</td>
                    </tr>
                    <tr class="bg-amber-500/5">
                      <td class="p-3 font-bold text-amber-400">Autonomy Scheduling</td>
                      <td class="p-3 text-rose-500">No</td>
                      <td class="p-3 text-rose-500">No</td>
                      <td class="p-3 text-rose-500">No</td>
                      <td class="p-3 text-rose-500">No</td>
                      <td class="p-3 text-emerald-400 font-bold">Yes (Trust scores schedule)</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

            <!-- Panel 6: Appendix -->
            <div id="panel-appendix" class="whitepaper-panel hidden space-y-6">
              <div class="border-l-4 border-amber-500 pl-4 py-1">
                <span class="font-mono text-xs text-amber-500 block uppercase">Appendix</span>
                <h3 class="text-2xl font-display font-bold text-white uppercase font-black">Compliance Mapping & Codified Blueprint</h3>
              </div>
              <p>The auditable, local controls implemented within Rogue1 Local map directly to standard corporate and government security frameworks:</p>
              <div class="grid grid-cols-1 md:grid-cols-3 gap-4 font-mono text-[11px] mb-6">
                <div class="p-4 bg-[#080B10] border border-[#1E293B]">
                  <strong class="text-cyan-400 block mb-1">NIST AI RMF / NIST SP 800 53</strong>
                  Satisfies AC 6 (Least Privilege), AU 12 (Audit), and CP 10 (System Recovery).
                </div>
                <div class="p-4 bg-[#080B10] border border-[#1E293B]">
                  <strong class="text-cyan-400 block mb-1">SOC 2 TYPE II / ISO 27001</strong>
                  Provides continuous operating controls and tamper proof logs.
                </div>
                <div class="p-4 bg-[#080B10] border border-[#1E293B]">
                  <strong class="text-cyan-400 block mb-1">EU AI ACT</strong>
                  Provides conformity assessments for high risk models via OPA pre execution gates.
                </div>
              </div>
            </div>

          </div>
        </div>
      </div>
    </section>
  </main>
"""

# HTML templates for the other pages
BUILDERS_PERMIT_HTML = """
  <main class="pt-28 pb-20 bg-[#080B10]">
    <div class="max-w-6xl mx-auto px-6">
      <div class="border-b border-[#1E293B] pb-12 mb-12 reveal">
        <span class="font-mono text-xs text-amber-500 uppercase tracking-widest block mb-2">Level 02 // Governance and Control</span>
        <h1 class="text-4xl sm:text-5xl font-display font-black text-white mb-4">The Builder's Permit Kernel</h1>
        <p class="text-slate-400 text-lg max-w-3xl leading-relaxed">
          An autonomous system can possess immense computational capability without automatically possessing authority. Within RogueOS, the Builder's Permit serves as the explicit operational passport required for every single execution.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-12 mb-16 reveal">
        <div class="space-y-4">
          <h3 class="text-xl font-display font-bold text-white uppercase font-black">The Authorization Failure of Modern AI</h3>
          <p class="text-slate-300 text-sm leading-relaxed">
            Standard software authentication verifies identity once at login. However, once authenticated, autonomous agents continue making decisions, generating tools, and calling database APIs long after. Traditional systems assume identity implies permission, allowing agents to run away, mutate states, and exceed operational scope without verification.
          </p>
        </div>
        <div class="space-y-4">
          <h3 class="text-xl font-display font-bold text-cyan-400 uppercase font-black">The Permit Solution</h3>
          <p class="text-slate-300 text-sm leading-relaxed">
            The Builder's Permit architecture models authority as a temporary, intent bounded, and closely scoped permission structure. Privileged operations are evaluated on demand against active organizational rules compiled as executable logic. If the permit's temporal duration, financial transaction limit, or resource boundaries are violated, execution instantly terminates.
          </p>
        </div>
      </div>

      <!-- THE 10 METADATA FIELDS -->
      <div class="mb-20 reveal">
        <div class="border-l-4 border-amber-500 pl-4 py-1 mb-8">
          <h2 class="text-2xl font-display font-bold text-white uppercase font-black">The 10 Standard Metadata Fields</h2>
          <p class="text-xs text-slate-400">Every Builder's Permit is cryptographically sealed and contains the following structural bounds:</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-4">
          <div class="p-5 bg-[#0F172A] border border-[#1E293B] hover:border-amber-500/50 transition-colors">
            <span class="font-mono text-amber-500 text-xs block mb-1">01 // UUID</span>
            <strong class="text-white text-xs block mb-2 uppercase">Permit Identifier</strong>
            <p class="text-[11px] text-slate-400">Globally unique cryptographic identifier assigned upon creation.</p>
          </div>
          <div class="p-5 bg-[#0F172A] border border-[#1E293B] hover:border-amber-500/50 transition-colors">
            <span class="font-mono text-amber-500 text-xs block mb-1">02 // Origin</span>
            <strong class="text-white text-xs block mb-2 uppercase">Request Origin</strong>
            <p class="text-[11px] text-slate-400">The initiating entity responsible for requesting execution.</p>
          </div>
          <div class="p-5 bg-[#0F172A] border border-[#1E293B] hover:border-amber-500/50 transition-colors">
            <span class="font-mono text-amber-500 text-xs block mb-1">03 // Intent</span>
            <strong class="text-white text-xs block mb-2 uppercase">Operational Intent</strong>
            <p class="text-[11px] text-slate-400">A normalized, machine evaluable representation of the objective.</p>
          </div>
          <div class="p-5 bg-[#0F172A] border border-[#1E293B] hover:border-amber-500/50 transition-colors">
            <span class="font-mono text-amber-500 text-xs block mb-1">04 // Scope</span>
            <strong class="text-white text-xs block mb-2 uppercase">Authorized Scope</strong>
            <p class="text-[11px] text-slate-400">Explicit boundaries (permitted directories, approved databases, APIs).</p>
          </div>
          <div class="p-5 bg-[#0F172A] border border-[#1E293B] hover:border-amber-500/50 transition-colors">
            <span class="font-mono text-amber-500 text-xs block mb-1">05 // Duration</span>
            <strong class="text-white text-xs block mb-2 uppercase">Temporal Duration</strong>
            <p class="text-[11px] text-slate-400">Maximum validity window. Expired permits instantly terminate execution.</p>
          </div>
          <div class="p-5 bg-[#0F172A] border border-[#1E293B] hover:border-amber-500/50 transition-colors">
            <span class="font-mono text-amber-500 text-xs block mb-1">06 // Constraints</span>
            <strong class="text-white text-xs block mb-2 uppercase">Resource Caps</strong>
            <p class="text-[11px] text-slate-400">Strict limitations on processor, RAM, network egress, and models.</p>
          </div>
          <div class="p-5 bg-[#0F172A] border border-[#1E293B] hover:border-amber-500/50 transition-colors">
            <span class="font-mono text-amber-500 text-xs block mb-1">07 // Risk Tier</span>
            <strong class="text-white text-xs block mb-2 uppercase">Risk Classification</strong>
            <p class="text-[11px] text-slate-400">Assessed impact tier determining the level of governance required.</p>
          </div>
          <div class="p-5 bg-[#0F172A] border border-[#1E293B] hover:border-amber-500/50 transition-colors">
            <span class="font-mono text-amber-500 text-xs block mb-1">08 // Approvals</span>
            <strong class="text-white text-xs block mb-2 uppercase">Required Approvals</strong>
            <p class="text-[11px] text-slate-400">Multisig signatures or human bypass keys based on risk level.</p>
          </div>
          <div class="p-5 bg-[#0F172A] border border-[#1E293B] hover:border-amber-500/50 transition-colors">
            <span class="font-mono text-amber-500 text-xs block mb-1">09 // Evidence</span>
            <strong class="text-white text-xs block mb-2 uppercase">Audit Bounds</strong>
            <p class="text-[11px] text-slate-400">Specific telemetry, spans, and evidence package configuration.</p>
          </div>
          <div class="p-5 bg-[#0F172A] border border-[#1E293B] hover:border-amber-500/50 transition-colors">
            <span class="font-mono text-amber-500 text-xs block mb-1">10 // Seals</span>
            <strong class="text-white text-xs block mb-2 uppercase">Integrity Verification</strong>
            <p class="text-[11px] text-slate-400">Cryptographic SHA256 signatures ensuring tamper proof lineage.</p>
          </div>
        </div>
      </div>
    </div>
  </main>
"""

ROGUEOS_HTML = """
  <main class="pt-28 pb-20 bg-[#080B10]">
    <div class="max-w-6xl mx-auto px-6">
      <div class="border-b border-[#1E293B] pb-12 mb-12 reveal">
        <span class="font-mono text-xs text-cyan-400 uppercase tracking-widest block mb-2">Level 03 // Research and Modular Computing</span>
        <h1 class="text-4xl sm:text-5xl font-display font-black text-white mb-4">RogueOS: The Trust Scheduler</h1>
        <p class="text-slate-400 text-lg max-w-3xl leading-relaxed">
          The ultimate boundary of enterprise safety is local independence. RogueOS is a local, forward deployed computing environment that schedules autonomous agency using live, calculated Trust as its core scheduling primitive.
        </p>
      </div>

      <div class="bg-[#0F172A] border border-[#1E293B] p-8 mb-16 reveal">
        <div class="max-w-3xl space-y-4">
          <div class="inline-flex items-center gap-2 px-3 py-1 bg-amber-500/10 border border-amber-500/30 text-amber-400 font-mono text-xs uppercase tracking-widest">
            A New Scheduling Paradigm
          </div>
          <h2 class="text-2xl sm:text-3xl font-display font-bold text-white uppercase font-black">Trust Is The Scheduler of Autonomy</h2>
          <p class="text-slate-300 text-sm leading-relaxed">
            In classical computer architecture, operating system schedulers allocate hardware threads, physical memory, and CPU clock cycles. They ask: <em>"Which process runs next?"</em>
          </p>
          <p class="text-slate-300 text-sm leading-relaxed font-bold">
            RogueOS asks a completely different question: <em>"Given this autonomous entity's demonstrated behavioral history, active operational context, and assigned mission, what is the highest level of autonomy it should be permitted to exercise right now?"</em>
          </p>
          <p class="text-slate-300 text-sm leading-relaxed">
            By modeling trust as a dynamic computational state (governed by live observation, compliance history, and progressive <strong>Trust Decay</strong> over time), RogueOS scales an agent's authority boundaries upward or downward dynamically. Autonomy is continuously earned, never statically assigned.
          </p>
        </div>
      </div>
    </div>
  </main>
"""

FRAMEWORK_HTML = """
  <main class="pt-28 pb-20 bg-[#080B10]">
    <div class="max-w-6xl mx-auto px-6">
      <div class="border-b border-[#1E293B] pb-12 mb-12 reveal">
        <span class="font-mono text-xs text-emerald-400 uppercase tracking-widest block mb-2">Operational Mathematics</span>
        <h1 class="text-4xl sm:text-5xl font-display font-black text-white uppercase mb-4">The Deterministic State Machine</h1>
        <p class="text-slate-400 text-lg max-w-3xl leading-relaxed">
          Uncontrolled agentic state changes generate unpredictability. RogueOS models and constraints runtime states through a formal, mathematically verified finite state machine.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-16 reveal">
        <div class="p-5 bg-[#0F172A] border border-[#1E293B]">
          <span class="font-mono text-emerald-400 text-xs block mb-2">01 // REQUESTED</span>
          <p class="text-xs text-slate-300">Execution task is submitted and canonical normalization is applied to input parameters.</p>
        </div>
        <div class="p-5 bg-[#0F172A] border border-[#1E293B]">
          <span class="font-mono text-emerald-400 text-xs block mb-2">02 // PENDING</span>
          <p class="text-xs text-slate-300">Identity verified, risk classification calculated, and active OPA policy evaluation is running.</p>
        </div>
        <div class="p-5 bg-[#0F172A] border border-[#1E293B]">
          <span class="font-mono text-emerald-400 text-xs block mb-2">03 // AUTHORIZED</span>
          <p class="text-xs text-slate-300">Execution satisfies all governance rules; a cryptographically signed Builder's Permit is issued.</p>
        </div>
        <div class="p-5 bg-[#0F172A] border border-[#1E293B]">
          <span class="font-mono text-emerald-400 text-xs block mb-2">04 // EXECUTING</span>
          <p class="text-xs text-slate-300">Workload schedules inside the isolated Docker/Firecracker container with resource limitations enforced.</p>
        </div>
        <div class="p-5 bg-[#0F172A] border border-[#1E293B]">
          <span class="font-mono text-rose-500 text-xs block mb-2">05 // RESTRICTED</span>
          <p class="text-xs text-slate-300">Active threat detection or context drift narrows the permitted scope boundaries during runtime.</p>
        </div>
        <div class="p-5 bg-[#0F172A] border border-[#1E293B]">
          <span class="font-mono text-rose-500 text-xs block mb-2">06 // SUSPENDED</span>
          <p class="text-xs text-slate-300">Execution pauses pending high level multisig human in the loop validation or context reconciliation.</p>
        </div>
        <div class="p-5 bg-[#0F172A] border border-[#1E293B]">
          <span class="font-mono text-rose-500 text-xs block mb-2">07 // REVOKED</span>
          <p class="text-xs text-slate-300">Authority terminates, executing sandboxes are terminated, and immediate stop work is enforced.</p>
        </div>
        <div class="p-5 bg-[#0F172A] border border-[#1E293B]">
          <span class="font-mono text-emerald-400 text-xs block mb-2">08 // ARCHIVED</span>
          <p class="text-xs text-slate-300">All logs, OTel traces, state checkpoints, and hashes are permanently sealed into the local ledger.</p>
        </div>
      </div>
    </div>
  </main>
"""

EVIDENCE_HTML = """
  <main class="pt-28 pb-20 bg-[#080B10]">
    <div class="max-w-6xl mx-auto px-6">
      <div class="border-b border-[#1E293B] pb-12 mb-12 reveal">
        <span class="font-mono text-xs text-cyan-400 uppercase tracking-widest block mb-2">Forensic Accountability</span>
        <h1 class="text-4xl sm:text-5xl font-display font-black text-white uppercase mb-4">The Evidence Ledger</h1>
        <p class="text-slate-400 text-lg max-w-3xl leading-relaxed">
          Standard logs are debugging aids generated as operational afterthoughts. RogueOS implements the Evidence Ledger as a core runtime primitive, preserving absolute audit chains.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-12 mb-16 reveal">
        <div class="space-y-4">
          <h3 class="text-xl font-display font-bold text-white uppercase font-black">The Flight Data Recorder Schema</h3>
          <p class="text-slate-300 text-sm leading-relaxed">
            Just like commercial aviation tracks and preserves complete system parameters inside crash survivable black boxes, RogueOS captures the complete operational state of an executing agent. This includes initial intent structures, specific model outputs, OPA query decisions, OTel span IDs, resource usage, and human supervision inputs.
          </p>
        </div>
        <div class="space-y-4">
          <h3 class="text-xl font-display font-bold text-cyan-400 uppercase font-black">RFC 6962 Compliant Integrity</h3>
          <p class="text-slate-300 text-sm leading-relaxed">
            Each evidence entry is processed through local SHA256 hash algorithms and appended to a cryptographic ledger conforming to transparent, tamper proof RFC 6962 tree structures. No records can be deleted, modified, or bypassed, guaranteeing courtroom ready digital evidence.
          </p>
        </div>
      </div>
    </div>
  </main>
"""

GLOSSARY_HTML = """
  <main class="pt-28 pb-20 bg-[#080B10]">
    <div class="max-w-6xl mx-auto px-6">
      <div class="border-b border-[#1E293B] pb-12 mb-12 reveal">
        <span class="font-mono text-xs text-amber-500 uppercase tracking-widest block mb-2">System Taxonomy</span>
        <h1 class="text-4xl sm:text-5xl font-display font-black text-white uppercase mb-4">Glossary of Terms</h1>
        <p class="text-slate-400 text-lg max-w-3xl leading-relaxed">
          The technical taxonomy of autonomous computing. Defining the specific engineering parameters that govern trust and execution.
        </p>
      </div>

      <div class="space-y-8 max-w-4xl reveal">
        <div>
          <strong class="text-amber-400 font-display text-lg block mb-1 font-black">The Builder's Permit</strong>
          <p class="text-sm text-slate-300 leading-relaxed">
            A dynamic, cryptographic permission token issued to authorize specific, short term operational objectives. It contains UUID, Scope Bounds, Temporal Duration, and Risk Classification parameters.
          </p>
        </div>
        <div>
          <strong class="text-amber-400 font-display text-lg uppercase block mb-1 font-black">Trust Decay</strong>
          <p class="text-sm text-slate-300 leading-relaxed">
            The mathematical reduction of calculated trust over time. As credentials age, environmental conditions drift, or threat variables fluctuate, authorization limits degrade naturally, forcing reverification.
          </p>
        </div>
        <div>
          <strong class="text-amber-400 font-display text-lg uppercase block mb-1 font-black">Trust Beacon</strong>
          <p class="text-sm text-slate-300 leading-relaxed">
            A dynamic digital signature emitted by active runtimes to broadcast their compliance profile, identity certificates, and active Builder's Permit parameters to neighboring collaborative systems.
          </p>
        </div>
        <div>
          <strong class="text-amber-400 font-display text-lg uppercase block mb-1 font-black">Independent Identity</strong>
          <p class="text-sm text-slate-300 leading-relaxed">
            A unique cryptographic tail number scheme assigned to autonomous participants, enabling continuous operational traceability across local, edge, and multi cloud environments.
          </p>
        </div>
        <div>
          <strong class="text-amber-400 font-display text-lg uppercase block mb-1 font-black">Canonical Normalization</strong>
          <p class="text-sm text-slate-300 leading-relaxed">
            The mathematical translation of unstructured external agent requests into a standardized, structured, machine evaluable representation before submitting to policy gates.
          </p>
        </div>
      </div>
    </div>
  </main>
"""

IMPLEMENTATION_HTML = """
  <main class="pt-28 pb-20 bg-[#080B10]">
    <div class="max-w-6xl mx-auto px-6">
      <div class="border-b border-[#1E293B] pb-12 mb-12 reveal">
        <span class="font-mono text-xs text-amber-500 uppercase tracking-widest block mb-2">Level 01 // Commercial Operations</span>
        <h1 class="text-4xl sm:text-5xl font-display font-black text-white uppercase mb-4">Enterprise Services</h1>
        <p class="text-slate-400 text-lg max-w-3xl leading-relaxed">
          How Stephen Zeitvogel and Rogue Management Group actually put autonomous systems to work safely inside corporate environments.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-16 reveal">
        <div class="bg-[#0F172A] border border-[#1E293B] p-8">
          <span class="font-mono text-xs text-amber-500 block mb-2">AUDITING // TIER ONE</span>
          <h3 class="text-2xl font-display font-bold text-white uppercase mb-4 font-black">AI Risk & Workflow Audits</h3>
          <p class="text-slate-300 text-sm leading-relaxed mb-6">
            A thorough assessment of your operational vulnerabilities, mapping your active agent workflows, software configurations, data boundaries, and vendor dependencies.
          </p>
          <p class="text-amber-400 font-bold font-mono text-lg">$2,500 Flat Fee</p>
        </div>
        <div class="bg-[#0F172A] border border-[#1E293B] p-8">
          <span class="font-mono text-xs text-emerald-400 block mb-2">DEVELOPMENT // TIER TWO</span>
          <h3 class="text-2xl font-display font-bold text-white uppercase mb-4 font-black">Governed Production Systems</h3>
          <p class="text-slate-300 text-sm leading-relaxed mb-6">
            Designing and coding bespoke, local first agent runtimes with built in Docker sandbox environments, SQLite state checkpoints, and custom OPA rules.
          </p>
          <p class="text-emerald-400 font-bold font-mono text-lg">Custom Pricing</p>
        </div>
        <div class="bg-[#0F172A] border border-[#1E293B] p-8">
          <span class="font-mono text-xs text-cyan-400 block mb-2">RETAINER // TIER THREE</span>
          <h3 class="text-2xl font-display font-bold text-white uppercase mb-4 font-black">Architectural Oversight</h3>
          <p class="text-slate-300 text-sm leading-relaxed mb-6">
            Ongoing code maintenance, policy audits, security patches, compliance reporting, and incident response support directly from our Charlotte HQ.
          </p>
          <p class="text-cyan-400 font-bold font-mono text-lg">Monthly Retainer</p>
        </div>
      </div>
    </div>
  </main>
"""

# ── DEDICATED ARCHITECT & BIO PAGE (UPGRADED TIES LEGACY) ──────────────────
ARCHITECT_HTML = """
  <main class="relative bg-[#080B10] overflow-hidden min-h-screen">
    <!-- Star trails celestial backdrop -->
    <div class="absolute top-0 left-0 w-full h-[65vh] z-0 overflow-hidden">
      <!-- Unsplash golden star trail background -->
      <img src="assets/img/hero-construction.jpg" class="w-full h-full object-cover opacity-20 filter contrast-125 saturate-150 transform scale-110 rotate-1">
      <div class="absolute inset-0 bg-gradient-to-t from-[#080B10] via-[#080B10]/80 to-transparent"></div>
    </div>

    <div class="relative z-10 max-w-6xl mx-auto px-6 pt-32 pb-24">
      <div class="border-b border-[#1E293B] pb-12 mb-16 reveal">
        <span class="font-mono text-xs text-amber-500 uppercase tracking-widest block mb-2">The Chief AI Solutions Architect // Charlotte HQ</span>
        <h1 class="text-4xl sm:text-6xl font-display font-black text-titanium uppercase mb-4 leading-none">Stephen Edmund Zeitvogel</h1>
        <p class="text-slate-400 text-lg max-w-3xl leading-relaxed">
          The multi generational story of an American builder. Rejecting the theoretical, coding the unbreakable, and securing accountable execution.
        </p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-start mb-20">
        <!-- Profile Column -->
        <div class="lg:col-span-4 space-y-6 reveal">
          <div class="bg-[#0F172A] border-2 border-[#1E293B] p-4 relative group hover:border-cyan-500/50 transition-all shadow-2xl">
            <!-- Neon Blue Wolf Icon as official RogueOS product seal overlay -->
            <div class="absolute -top-3 -right-3 w-10 h-10 bg-[#080B10] border border-cyan-500 rounded flex items-center justify-center glow-cyan">
              <i data-lucide="shield-check" class="w-5 h-5 text-cyan-400 animate-pulse"></i>
            </div>
            <!-- Standard placeholder image with professional overlay -->
            <div class="w-full h-[480px] bg-black relative overflow-hidden rounded mb-4">
              <img src="assets/img/architect-stephen.jpg" alt="Stephen Zeitvogel Portrait" class="w-full h-full object-cover object-top filter contrast-110">
              <div class="absolute inset-0 bg-gradient-to-t from-[#0F172A] via-transparent to-transparent"></div>
            </div>
            <strong class="text-white block uppercase font-display text-lg tracking-wider">Stephen E. Zeitvogel</strong>
            <span class="font-mono text-xs text-amber-400 tracking-widest uppercase">Founder & Chief Solutions Architect</span>
            <span class="font-mono text-[10px] text-slate-500 block mt-1 uppercase">Charlotte, North Carolina</span>
          </div>

          <!-- PROOF CARDS -->
          <div class="bg-black/40 border border-[#1E293B] p-6 space-y-4 font-mono text-xs">
            <div class="flex items-center gap-2 text-white font-bold uppercase border-b border-[#1E293B] pb-2">
              <i data-lucide="folder-git" class="w-4 h-4 text-amber-500"></i>
              Verified Evidence & IP Shield
            </div>
            <!-- 2008 LLC Proof -->
            <div class="p-3 bg-[#0F172A]/80 border border-slate-800 rounded">
              <span class="text-amber-500 font-bold block mb-1">NC SOS ID: 0846824</span>
              <p class="text-slate-300 text-[10px] leading-relaxed">
                RJZ Enterprises, LLC registered in North Carolina in 2008. Nearly two decades of physical logistical, medical, and technology management presence in Charlotte.
              </p>
            </div>
            <!-- USPTO Proof -->
            <div class="p-3 bg-[#0F172A]/80 border border-slate-800 rounded">
              <span class="text-cyan-400 font-bold block mb-1">USPTO Application 63/864,057</span>
              <p class="text-slate-300 text-[10px] leading-relaxed">
                Provisional utility patent filed December 14, 2025 for "Rogue AgentOS", protecting the sequence specific (A to F) human in the loop runtime paradigm.
              </p>
            </div>
          </div>
        </div>

        <!-- Narrative Column -->
        <div class="lg:col-span-8 space-y-8 reveal text-slate-300 text-sm leading-relaxed">
          <div class="space-y-4">
            <h3 class="text-2xl font-display font-bold text-white uppercase font-black tracking-tight">
              I. The Winston Salem Legacy: From Beverages to Binary
            </h3>
            <p>
              Stephen did not learn systems architecture from an academic textbook or a venture capital pitch deck. His education began in Winston Salem, North Carolina, watching his father, <strong>Richard Joseph Zeitvogel</strong>, manage and expand <strong>Alpine Beverage Distributing, Inc.</strong> Alpine Beverage lived and died by its routes, its physical delivery enclaves, its strict timetables, and its logistical accountability.
            </p>
            <p>
              RogueOS is the direct translation of this multi generational logistical discipline into autonomous software. A beverage truck cannot exit its route or distribute payloads without a localized manifest and explicit authority. Within RogueOS, an autonomous agent cannot write database modifications, execute financial commands, or utilize resources without possessing a cryptographically signed **Builder's Permit**. We treat digital agency exactly like industrial logistics.
            </p>
          </div>

          <div class="space-y-4">
            <h3 class="text-2xl font-display font-bold text-white uppercase font-black tracking-tight">
              II. Rebuilt From Zero: Stone Cold Sobriety and True Grit
            </h3>
            <p>
              The technology sector is saturated with over privileged founders who have never faced system level failures. Stephen’s design philosophy was forged through hard, forensic survival. Following the death of his father in 2012, Stephen faced an onslaught of legal battles. Stepmother Catherine Zeitvogel, guided by a single self dealing attorney, hid the multi million dollar estate, and leaked trust funds in a preferential insider loan surfacing only in brother Rick's 2024 divorce.
            </p>
            <p>
              Simultaneously, a false ex parte protective order exploitation by a covert narcissist led to Stephen being evicted from his apartment, losing his job, and having his TSA credentials taken. Forced to move back into a bedroom at his mother's house, Stephen had every excuse to sit on the sofa and declare that life wasn't fair.
            </p>
            <div class="p-6 bg-[#0F172A] border-l-4 border-amber-500 my-6">
              <strong class="text-white uppercase font-display block mb-2 tracking-wide font-black">
                The Private Standard of Control
              </strong>
              <p class="italic text-slate-200 text-sm leading-relaxed">
                "I took away every excuse. I stayed sober through a decade long family betrayal and a multi county legal war. I sat in that bedroom and coded a deterministic operating kernel that forces computers to prove their execution before they act. If I can build a patented software fortress from that bedroom, you have zero excuses to remain on the sofa."
              </p>
            </div>
            <p>
              RogueOS is structured to prevent exactly what Stephen witnessed in family court, probate, and corporate wrappers: the manipulation of state records. Every decision, every validation, and every rollback in our system is rendered tamper proof, chronologically ordered, and completely **court admissible**.
            </p>
          </div>

          <div class="space-y-4">
            <h3 class="text-2xl font-display font-bold text-white uppercase font-black tracking-tight">
              III. Jackie Diesel: The Jaded Edge of Music and Control
            </h3>
            <p>
              When he is not designing policy as code kernels, Stephen is a singer, songwriter, and guitar player operating under the stage name **Jackie Diesel**. The raw rasp in his voice, the jaded edge in his gait, and the chip on his shoulder don’t come from a marketing agency, they come from living the truth.
            </p>
            <p class="font-bold text-amber-400">
              "NEVER LET GO OF YOUR DREAMS. JUST GET A DAY JOB AND CHANGE THE PLAN ON HOW TO GET THERE!"
            </p>
            <p>
              RMG is that day job engine. It is the technical fortress that funds Stephen’s independence and protects his artistic freedom, showing the younger generation how to use high consequence engineering to fuel their creative dreams without ever asking corporate bosses or record labels for permission.
            </p>
          </div>
        </div>
      </div>
    </div>
  </main>
"""

# ── TRADES & AMERICAN BUILD PAGE (UPGRADED MIKE ROWE LINK) ───────────────
TRADES_HTML = """
  <main class="pt-28 pb-20 bg-[#080B10]">
    <div class="max-w-6xl mx-auto px-6">
      <div class="border-b border-[#1E293B] pb-12 mb-12 reveal">
        <span class="font-mono text-xs text-amber-500 uppercase tracking-widest block mb-2">Social and Industrial Mission</span>
        <h1 class="text-4xl sm:text-5xl font-display font-black text-white uppercase mb-4">The American Build</h1>
        <p class="text-slate-400 text-lg max-w-3xl leading-relaxed">
          Bringing discipline, craft, and physical construction principles back into high technology software development.
        </p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-start mb-16 reveal">
        <div class="lg:col-span-7 space-y-6">
          <div class="p-6 bg-amber-500/10 border border-amber-500/30 glow-amber">
            <p class="font-display font-black text-2xl text-amber-400 uppercase tracking-wide text-center">
              "Get Off The Sofa. Pick Up A Tool."
            </p>
          </div>
          <p class="text-slate-300 text-sm leading-relaxed">
            Modern software development has become lazy, cloud tethered, and fragile. Stephen believes software development must mirror the exact, disciplined vocational trades: carpentry, steelworking, plumbing, and aviation maintenance. RogueOS is manual labor for the software era. No corporate handouts, no cloud monopolies, just raw, local, independent engineering.
          </p>
          <p class="text-slate-300 text-sm leading-relaxed">
            By building systems that are offline, deterministic, and root governed, we train a new breed of developers: the digital craftsmen. These are individuals who take pride in writing code that can execute on raw local hardware without asking permission from corporate server farms.
          </p>

          <!-- The Mike Rowe works Hook -->
          <div class="bg-[#0F172A] border border-[#1E293B] p-8 mt-12 rounded relative overflow-hidden">
            <div class="absolute -top-3 -right-3 w-12 h-12 bg-[#080B10] border border-amber-500/50 rounded flex items-center justify-center">
              <i data-lucide="wrench" class="w-5 h-5 text-amber-500"></i>
            </div>
            <h3 class="text-xl font-display font-black text-white uppercase mb-4">Supporting the mikeroweWORKS Foundation</h3>
            <p class="text-slate-300 text-xs leading-relaxed mb-6">
              We actively support the **mikeroweWORKS Foundation** in their mission to close the skills gap, challenge the dynamic that puts white collar work on a pedestal above trades, and restore the value of hard work.
            </p>
            <div class="p-5 bg-black/40 border border-slate-800 rounded font-mono text-[11px] text-slate-300 mb-6">
              <span class="text-amber-500 font-bold block mb-2 uppercase">A Direct Call to Mike Rowe:</span>
              "Mike, you have spent decades telling America to get off the sofa and pick up a tool. We built the tool for the next fifty years of computing. This is digital physical work, built by tradesmen, governed by the loop. Let's close the digital skills gap together."
            </div>
            <a href="https://www.mikeroweworks.org" target="_blank" class="inline-block bg-amber-500 hover:bg-amber-400 text-black font-mono text-xs font-bold uppercase tracking-wider px-6 py-3 transition-all">Support mikeroweWORKS ↗</a>
          </div>
        </div>

        <!-- Sidebar / Statistics -->
        <div class="lg:col-span-5 bg-[#0F172A] border border-[#1E293B] p-8 rounded space-y-6">
          <h4 class="font-display font-bold text-white uppercase text-lg tracking-wider border-b border-[#1E293B] pb-3">The Skills Pipeline</h4>
          <p class="text-xs text-slate-400 leading-relaxed">
            The next generation of builders isn't waiting on corporate approvals. They are writing code on single workstations, setting up isolated enclaves, and recovering control over their digital tools.
          </p>
          <div class="space-y-4">
            <div class="p-4 bg-black/40 border border-slate-800 rounded">
              <span class="text-amber-500 font-mono text-xs block mb-1">01 / LOCAL INITIATIVE</span>
              <p class="text-[11px] text-slate-300 leading-normal">Building tools that run offline, removing reliance on multi billion dollar cloud monopolies.</p>
            </div>
            <div class="p-4 bg-black/40 border border-slate-800 rounded">
              <span class="text-cyan-400 font-mono text-xs block mb-1">02 / HARDENED DISCIPLINE</span>
              <p class="text-[11px] text-slate-300 leading-normal">Applying standard checklist procedures from commercial aviation directly into development.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
"""

CONTACT_HTML = """
  <main class="pt-28 pb-20 bg-[#080B10]">
    <div class="max-w-6xl mx-auto px-6">
      <div class="border-b border-[#1E293B] pb-12 mb-12 reveal">
        <span class="font-mono text-xs text-cyan-400 uppercase tracking-widest block mb-2">Inquiry Routing</span>
        <h1 class="text-4xl sm:text-5xl font-display font-black text-white uppercase mb-4">Open The Channel</h1>
        <p class="text-slate-400 text-lg max-w-3xl leading-relaxed">
          Connect directly with Stephen Zeitvogel and our Charlotte based engineering office.
        </p>
      </div>

      <div class="max-w-2xl bg-[#0F172A] border border-[#1E293B] p-8 rounded shadow-xl reveal">
        <form action="mailto:stephen.zeitvogel@roguemgmtgroup.com" method="POST" enctype="text/plain" class="space-y-6 font-mono text-xs">
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
            <div>
              <label class="text-slate-400 block mb-2 uppercase font-bold">Your Name</label>
              <input type="text" name="name" required class="w-full bg-[#080B10] border border-[#1E293B] p-3 text-white focus:outline-none focus:border-amber-500">
            </div>
            <div>
              <label class="text-slate-400 block mb-2 uppercase font-bold">Your Email</label>
              <input type="email" name="email" required class="w-full bg-[#080B10] border border-[#1E293B] p-3 text-white focus:outline-none focus:border-amber-500">
            </div>
          </div>
          <div>
            <label class="text-slate-400 block mb-2 uppercase font-bold">Inquiry Type</label>
            <select name="inquiry_type" class="w-full bg-[#080B10] border border-[#1E293B] p-3 text-white focus:outline-none focus:border-amber-500">
              <option value="audit">Tier One AI Risk & Workflow Audit ($2,500)</option>
              <option value="governed_sys">Governed Production Systems (Level 2/3)</option>
              <option value="licensing">Licensing Builder's Permit Specifications</option>
              <option value="music">Sponsorship / Career Collaboration</option>
            </select>
          </div>
          <div>
            <label class="text-slate-400 block mb-2 uppercase font-bold">Details</label>
            <textarea name="details" rows="5" required class="w-full bg-[#080B10] border border-[#1E293B] p-3 text-white focus:outline-none focus:border-amber-500"></textarea>
          </div>
          <button type="submit" class="w-full bg-amber-500 hover:bg-amber-400 text-black font-bold uppercase tracking-wider py-4 transition-all">Submit Secure Payload</button>
        </form>
      </div>
    </div>
  </main>
"""

# ── COMPILER FUNCTIONS ──────────────────────────────────────────────────


def process_images():
    print("[*] Initiating high fidelity local visual asset build...")
    
    # 1. Look for Stephen's uploaded founder portrait
    extensions = ['.jpg', '.jpeg', '.png', '.webp']
    found_profile_path = None
    
    # Look for exact match in current directory (Downloads)
    for ext in extensions:
        test_path = f"stephen-zeitvogel-rmg-founder-charlotte-office{ext}"
        if os.path.exists(test_path):
            found_profile_path = test_path
            break
            
    # Look for case-insensitive match
    if not found_profile_path:
        for filename in os.listdir('.'):
            if filename.lower().startswith('stephen-zeitvogel-rmg-founder-charlotte-office'):
                found_profile_path = filename
                break
                
    os.makedirs('assets/img', exist_ok=True)
    target_profile = os.path.join('assets', 'img', 'architect-stephen.jpg')
    
    if found_profile_path:
        print(f"[+] Detected profile photo: {found_profile_path}")
        try:
            img = Image.open(found_profile_path)
            if img.mode != 'RGB':
                img = img.convert('RGB')
                
            # Write appropriate metadata and keywords to this photo
            exif = img.getexif()
            exif[270] = "Stephen Zeitvogel, Founder and Chief AI Solutions Architect of Rogue Management Group, LLC, based in Charlotte, NC."
            exif[315] = "Stephen Zeitvogel"
            exif[305] = "RMG Website Compiler v7"
            exif[37510] = b"ASCII\x00\x00\x00RMG Founder Photo - Charlotte NC - Keywords: AI Governance, RogueOS, Builder's Permit, Winston-Salem, Alpine Beverage, Jackie Diesel, American Build, Independent AI, Active Runtime"
            
            # Save the processed image directly to the target location
            img.save(target_profile, "JPEG", quality=95, exif=exif)
            print(f"[+] Successfully processed, added SEO metadata, and saved profile image to {target_profile}")
        except Exception as e:
            print(f"[!] Error processing profile photo: {e}")
            generate_default_profile(target_profile)
    else:
        print("[!] Profile photo 'stephen-zeitvogel-rmg-founder-charlotte-office' not found in current folder.")
        print("[!] Generating high end professional default profile visual...")
        generate_default_profile(target_profile)
        
    # 2. Process or generate hero background visual
    target_hero = os.path.join('assets', 'img', 'hero-construction.jpg')
    found_hero_path = None
    for ext in extensions:
        test_path = f"hero-construction{ext}"
        if os.path.exists(test_path):
            found_hero_path = test_path
            break
            
    if found_hero_path:
        print(f"[+] Detected local hero background: {found_hero_path}")
        try:
            img = Image.open(found_hero_path)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img.save(target_hero, "JPEG", quality=90)
            print(f"[+] Saved hero background to {target_hero}")
        except Exception as e:
            print(f"[!] Error processing hero background: {e}")
            generate_default_hero(target_hero)
    else:
        print("[!] Local 'hero-construction' background image not found.")
        print("[!] Generating professional high contrast amber star trail visual...")
        generate_default_hero(target_hero)

def generate_default_profile(target_path):
    # Generates a premium dark vector layout with custom technical grids
    try:
        img = Image.new("RGB", (480, 600), "#080B10")
        draw = ImageDraw.Draw(img)
        # Background matrix grids
        for x in range(0, 480, 40):
            draw.line([x, 0, x, 600], fill="#1E293B", width=1)
        for y in range(0, 600, 40):
            draw.line([0, y, 480, y], fill="#1E293B", width=1)
        # Industrial accents
        draw.rectangle([20, 20, 460, 580], outline="#1E293B", width=2)
        draw.rectangle([30, 30, 450, 570], outline="#F59E0B", width=1)
        # Text details
        draw.text((50, 280), "STEPHEN ZEITVOGEL", fill="#FFFFFF")
        draw.text((50, 310), "CHIEF AI ARCHITECT", fill="#38BDF8")
        draw.text((50, 330), "RMG FOUNDER", fill="#F59E0B")
        img.save(target_path, "JPEG", quality=95)
        print(f"[+] Default profile visual written to {target_path}")
    except Exception as e:
        print(f"[!] Failed to generate profile placeholder: {e}")

def generate_default_hero(target_path):
    # Generates a stunning dark background with custom amber light trails and grid nodes
    try:
        img = Image.new("RGB", (1920, 1080), "#080B10")
        draw = ImageDraw.Draw(img)
        # Technical grid lines
        for x in range(0, 1920, 80):
            draw.line([x, 0, x, 1080], fill="#0F172A", width=1)
        for y in range(0, 1080, 80):
            draw.line([0, y, 1920, y], fill="#0F172A", width=1)
        # Programmatic long exposure golden star trails
        import math
        for i in range(150):
            # Draw diagonal light trails
            cx = (i * 35) % 1920
            cy = (i * 15) % 1080
            length = 200 + (i % 5) * 50
            draw.line([cx, cy, cx + length, cy + (length * 0.3)], fill="#F59E0B", width=1)
        img.save(target_path, "JPEG", quality=90)
        print(f"[+] Premium default hero backdrop written to {target_path}")
    except Exception as e:
        print(f"[!] Failed to generate hero placeholder: {e}")


def register_site_files():
    # Create asset directory structures
    dirs = ['assets/css', 'assets/js', 'assets/img', 'docs']
    for d in dirs:
        if not os.path.exists(d):
            os.makedirs(d)
            print(f"[+] Created directory: {d}")

    # Write CSS Core stylesheet
    with open('assets/css/rm-core.css', 'w', encoding='utf-8') as f:
        f.write(css_content_data())
    print("[+] Written: assets/css/rm-core.css")

    # Write JS App code
    with open('assets/js/rm-app.js', 'w', encoding='utf-8') as f:
        f.write(js_content_data())
    print("[+] Written: assets/js/rm-app.js")

def css_content_data():
    return """/* RMG Industrial Design System Core Styles */
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Manrope:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap');

/* Scroll-Trigger Animations */
.reveal {
  opacity: 0;
  transform: translateY(35px);
  transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1), transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}
.reveal.active {
  opacity: 1;
  transform: translateY(0);
}

/* Radar & Industrial Glows (Golden Pulse and Interactive Enhancements) */
.glow-amber {
  box-shadow: 0 0 35px rgba(245, 158, 11, 0.25);
  transition: box-shadow 0.3s ease-in-out, border-color 0.3s ease-in-out, transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}
.glow-amber:hover {
  box-shadow: 0 0 50px rgba(245, 158, 11, 0.55);
  border-color: rgba(245, 158, 11, 0.6) !important;
  transform: translateY(-2px);
}
.glow-cyan {
  box-shadow: 0 0 35px rgba(56, 189, 248, 0.25);
  transition: box-shadow 0.3s ease-in-out, border-color 0.3s ease-in-out, transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}
.glow-cyan:hover {
  box-shadow: 0 0 50px rgba(56, 189, 248, 0.55);
  border-color: rgba(56, 189, 248, 0.6) !important;
  transform: translateY(-2px);
}
.glow-emerald {
  box-shadow: 0 0 35px rgba(16, 185, 129, 0.25);
  transition: box-shadow 0.3s ease-in-out, border-color 0.3s ease-in-out, transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}
.glow-emerald:hover {
  box-shadow: 0 0 50px rgba(16, 185, 129, 0.55);
  border-color: rgba(16, 185, 129, 0.6) !important;
  transform: translateY(-2px);
}
.glow-rose {
  box-shadow: 0 0 35px rgba(239, 68, 68, 0.25);
  transition: box-shadow 0.3s ease-in-out, border-color 0.3s ease-in-out, transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}
.glow-rose:hover {
  box-shadow: 0 0 50px rgba(239, 68, 68, 0.55);
  border-color: rgba(239, 68, 68, 0.6) !important;
  transform: translateY(-2px);
}

/* Custom Scrollbar */
::-webkit-scrollbar {
  width: 8px;
}
::-webkit-scrollbar-track {
  background: #080B10;
}
::-webkit-scrollbar-thumb {
  background: #1E293B;
  border-radius: 4px;
}
::-webkit-scrollbar-thumb:hover {
  background: #F59E0B;
}

#construction-canvas {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
  pointer-events: none;
}
"""

def js_content_data():
    return """/* RMG Active Runtime & UI Orchestrator */
document.addEventListener('DOMContentLoaded', () => {
  // Mobile Menu Drawer Trigger
  const mobileMenuBtn = document.getElementById('mobile-menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');

  if (mobileMenuBtn && mobileMenu) {
    mobileMenuBtn.addEventListener('click', () => {
      mobileMenu.classList.toggle('hidden');
      mobileMenu.classList.toggle('flex');
    });
  }

  // Lucide Icons Initialization
  if (typeof lucide !== 'undefined') {
    lucide.createIcons();
  }

  // Scroll-Trigger Reveal Observer
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
      }
    });
  }, { threshold: 0.15 });

  document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

  // Dynamic Terminal Logging Feed Simulation (Grounded OPA Executions)
  const terminalFeed = document.getElementById('terminal-feed');
  if (terminalFeed) {
    const logs = [
      { text: "sys_verify: Checking local multisig authority keys... [VALIDATED]", class: "text-emerald-400" },
      { text: "consensus_arbiter: 3/3 local models reached mathematical agreement.", class: "text-slate-300" },
      { text: "sha256_hash: f6590bc39e1f8d4c... [IMMUTABLE WAL RECORD LOCKED]", class: "text-amber-400" },
      { text: "OPA Policy Gate Check: input.tool='echo', input.net_egress=false... [ALLOW]", class: "text-emerald-400" },
      { text: "OTel Span Exported: rogue.run [ID: 7298aa23]", class: "text-cyan-400" },
      { text: "Checkpoint Created: SQLite State [UUID: f6590bc3-9e1f-4d4c]", class: "text-slate-300" },
      { text: "sys_verify: Querying local Trust Beacon... CURRENT STATE = 1.0 (Earned)", class: "text-cyan-400" },
      { text: "policy_gate: Checking PII / data leak filters... PASS (no_pii detected)", class: "text-emerald-400" },
      { text: "Docker Sandbox initialized in read-only mode with zero network access.", class: "text-slate-400" },
      { text: "Rogue1 Local execution loop active. Control confirmed.", class: "text-amber-500 font-bold" }
    ];

    let index = 3;
    setInterval(() => {
      const log = logs[index % logs.length];
      const p = document.createElement('p');
      p.innerHTML = `<span class="text-slate-500">></span> ${log.text}`;
      if (log.class) p.className = log.class;
      terminalFeed.appendChild(p);
      
      if (terminalFeed.children.length > 8) {
        terminalFeed.removeChild(terminalFeed.firstChild);
      }
      index++;
    }, 4000);
  }

  // Background animation
  const canvas = document.getElementById('construction-canvas');
  if (canvas) {
    const ctx = canvas.getContext('2d');
    let width, height, points = [];

    function resize() {
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
      points = [];
      for (let i = 0; i < 35; i++) {
        points.push({
          x: Math.random() * width,
          y: Math.random() * height,
          vx: (Math.random() - 0.5) * 0.8,
          vy: (Math.random() - 0.5) * 0.8
        });
      }
    }
    window.addEventListener('resize', resize);
    resize();

    function draw() {
      ctx.clearRect(0, 0, width, height);
      ctx.strokeStyle = 'rgba(245, 158, 11, 0.15)';
      ctx.lineWidth = 1;

      for (let i = 0; i < points.length; i++) {
        let p = points[i];
        p.x += p.vx;
        p.y += p.vy;

        if (p.x < 0 || p.x > width) p.vx *= -1;
        if (p.y < 0 || p.y > height) p.vy *= -1;

        ctx.fillStyle = 'rgba(56, 189, 248, 0.4)';
        ctx.fillRect(p.x - 2, p.y - 2, 4, 4);

        for (let j = i + 1; j < points.length; j++) {
          let p2 = points[j];
          let dist = Math.hypot(p.x - p2.x, p.y - p2.y);
          if (dist < 180) {
            ctx.beginPath();
            ctx.moveTo(p.x, p.y);
            ctx.lineTo(p2.x, p2.y);
            ctx.stroke();
          }
        }
      }
      requestAnimationFrame(draw);
    }
    draw();
  }
});

window.switchTab = function(tabId) {
  document.querySelectorAll('.whitepaper-panel').forEach(panel => {
    panel.classList.add('hidden');
  });
  document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.classList.remove('border-amber-500', 'text-amber-400');
    btn.classList.add('border-transparent', 'text-slate-400');
  });

  const activePanel = document.getElementById(`panel-${tabId}`);
  if (activePanel) activePanel.classList.remove('hidden');

  const activeBtn = document.getElementById(`btn-${tabId}`);
  if (activeBtn) {
    activeBtn.classList.remove('border-transparent', 'text-slate-400');
    activeBtn.classList.add('border-amber-500', 'text-amber-400');
  }
}
"""

def append_index_html():
    full_index = SHARED_HEADER + INDEX_HTML_CONTENT + SHARED_FOOTER
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(full_index)
    print("[+] Successfully compiled and blended new blueprint into index.html")

def append_other_pages():
    pages = {
        'builders-permit.html': BUILDERS_PERMIT_HTML,
        'rogueos.html': ROGUEOS_HTML,
        'framework.html': FRAMEWORK_HTML,
        'evidence.html': EVIDENCE_HTML,
        'glossary.html': GLOSSARY_HTML,
        'implementation.html': IMPLEMENTATION_HTML,
        'architect.html': ARCHITECT_HTML,
        'trades.html': TRADES_HTML,
        'contact.html': CONTACT_HTML
    }

    for name, content in pages.items():
        full_html = SHARED_HEADER + content + SHARED_FOOTER
        with open(name, 'w', encoding='utf-8') as f:
            f.write(full_html)
        print(f"[+] Written and compiled: {name}")

    # Auxiliary config files
    with open('netlify.toml', 'w', encoding='utf-8') as f:
        f.write('[[redirects]]\\n  from = "/*"\\n  to = "index.html"\\n  status = 200\\n')
    print("[+] Written: netlify.toml")

    with open('_redirects', 'w', encoding='utf-8') as f:
        f.write('/* /index.html 200\\n')
    print("[+] Written: _redirects")

    with open('robots.txt', 'w', encoding='utf-8') as f:
        f.write('User-agent: *\\nAllow: /\\n')
    print("[+] Written: robots.txt")

    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\\n  <url><loc>https://roguemgmtgroup.com/index.html</loc></url>\\n  <url><loc>https://roguemgmtgroup.com/builders-permit.html</loc></url>\\n  <url><loc>https://roguemgmtgroup.com/rogueos.html</loc></url>\\n  <url><loc>https://roguemgmtgroup.com/framework.html</loc></url>\\n  <url><loc>https://roguemgmtgroup.com/evidence.html</loc></url>\\n  <url><loc>https://roguemgmtgroup.com/glossary.html</loc></url>\\n  <url><loc>https://roguemgmtgroup.com/implementation.html</loc></url>\\n  <url><loc>https://roguemgmtgroup.com/architect.html</loc></url>\\n  <url><loc>https://roguemgmtgroup.com/trades.html</loc></url>\\n  <url><loc>https://roguemgmtgroup.com/contact.html</loc></url>\\n</urlset>\\n')
    print("[+] Written: sitemap.xml")

if __name__ == "__main__":
    process_images()
    register_site_files()
    append_index_html()
    append_other_pages()
    print("\\n==================================================")
    print("  ROGUE WEBSITE COMPILER SUCCESSFUL!")
    print("==================================================")
    print("[!] Run this script on your local workstation to compile your web server.")
