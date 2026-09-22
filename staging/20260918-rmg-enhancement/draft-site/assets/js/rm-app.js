/* RMG Active Runtime & UI Orchestrator */
document.addEventListener('DOMContentLoaded', () => {
  // Mobile Menu Drawer Trigger
  const mobileMenuBtn = document.getElementById('mobile-menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');

  if (mobileMenuBtn && mobileMenu) {
    const setMenuState = (isOpen) => {
      mobileMenu.classList.toggle('hidden', !isOpen);
      mobileMenu.classList.toggle('flex', isOpen);
      mobileMenuBtn.setAttribute('aria-expanded', String(isOpen));
      mobileMenuBtn.setAttribute('aria-label', isOpen ? 'Close navigation menu' : 'Open navigation menu');
    };

    mobileMenuBtn.addEventListener('click', () => {
      setMenuState(mobileMenu.classList.contains('hidden'));
    });

    mobileMenu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => setMenuState(false));
    });

    document.addEventListener('keydown', event => {
      if (event.key === 'Escape' && !mobileMenu.classList.contains('hidden')) {
        setMenuState(false);
        mobileMenuBtn.focus();
      }
    });
  }

  // Hero Video Sound Toggle (browsers block autoplay-with-audio, so muted
  // autoplay is required; this lets a visitor opt in to sound with one click)
  const heroVideo = document.getElementById('hero-video');
  const soundToggle = document.getElementById('hero-sound-toggle');

  if (heroVideo && soundToggle) {
    const labelEl = soundToggle.querySelector('span');
    const iconOff = soundToggle.querySelector('.hero-sound-icon-off');
    const iconOn = soundToggle.querySelector('.hero-sound-icon-on');

    const setSoundState = (isOn) => {
      heroVideo.muted = !isOn;
      soundToggle.setAttribute('aria-pressed', String(isOn));
      soundToggle.setAttribute('aria-label', isOn ? 'Turn hero video sound off' : 'Turn hero video sound on');
      if (labelEl) {
        labelEl.textContent = isOn ? 'Sound off' : 'Sound on';
      }
      if (iconOff && iconOn) {
        iconOff.classList.toggle('hidden', isOn);
        iconOn.classList.toggle('hidden', !isOn);
      }
    };

    soundToggle.addEventListener('click', () => {
      const turningOn = heroVideo.muted;
      if (turningOn) {
        heroVideo.play().catch(() => {});
      }
      setSoundState(turningOn);
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
