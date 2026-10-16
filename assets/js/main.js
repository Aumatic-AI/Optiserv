/* Optiserv Consulting — "Signal"
   Vanilla, dependency-free. Every enhancement degrades: with JS off the page
   stays readable, navigable and submittable. */
(function () {
  'use strict';

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $  = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* ---------------------------------------------------------- header */
  var hdr = $('#hdr');
  if (hdr) {
    var onScroll = function () { hdr.classList.toggle('is-stuck', window.scrollY > 8); };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* -------------------------------------------------------- dropdown */
  $$('.nav-trigger').forEach(function (trigger) {
    var panel = document.getElementById(trigger.getAttribute('aria-controls'));
    if (!panel) return;
    var item = trigger.closest('li');
    var timer;

    var open = function (on) {
      trigger.setAttribute('aria-expanded', String(on));
      panel.classList.toggle('is-open', on);
    };

    trigger.addEventListener('click', function (e) {
      e.preventDefault();
      open(trigger.getAttribute('aria-expanded') !== 'true');
    });
    item.addEventListener('mouseenter', function () { clearTimeout(timer); open(true); });
    item.addEventListener('mouseleave', function () { timer = setTimeout(function () { open(false); }, 140); });
    item.addEventListener('focusout', function () {
      setTimeout(function () { if (!item.contains(document.activeElement)) open(false); }, 0);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && trigger.getAttribute('aria-expanded') === 'true') { open(false); trigger.focus(); }
    });
    document.addEventListener('click', function (e) { if (!item.contains(e.target)) open(false); });
  });

  /* ---------------------------------------------------------- drawer */
  var burger = $('.burger');
  var drawer = $('#drawer');
  if (burger && drawer) {
    drawer.hidden = false;                       /* only now that JS runs */
    var lastFocus = null;

    var setDrawer = function (on) {
      burger.setAttribute('aria-expanded', String(on));
      burger.setAttribute('aria-label', on ? 'Close menu' : 'Open menu');
      drawer.classList.toggle('is-open', on);
      document.body.style.overflow = on ? 'hidden' : '';
      if (on) {
        lastFocus = document.activeElement;
        var first = $('a, button', drawer);
        if (first) first.focus();
      } else if (lastFocus) {
        lastFocus.focus();
      }
    };

    burger.addEventListener('click', function () {
      setDrawer(burger.getAttribute('aria-expanded') !== 'true');
    });
    $$('a', drawer).forEach(function (a) { a.addEventListener('click', function () { setDrawer(false); }); });

    document.addEventListener('keydown', function (e) {
      if (burger.getAttribute('aria-expanded') !== 'true') return;
      if (e.key === 'Escape') { setDrawer(false); return; }
      if (e.key !== 'Tab') return;
      var items = $$('a, button', drawer).filter(function (el) { return el.offsetParent !== null; });
      if (!items.length) return;
      var first = items[0], last = items[items.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    });

    window.addEventListener('resize', function () {
      if (window.innerWidth > 1060 && burger.getAttribute('aria-expanded') === 'true') setDrawer(false);
    });
  }

  /* ---------------------------------------------------------- reveal */
  var revealables = $$('[data-reveal]');
  if (!('IntersectionObserver' in window) || reduced) {
    revealables.forEach(function (el) { el.classList.add('is-in'); });
  } else {
    var ro = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-in');
        ro.unobserve(entry.target);
      });
    }, { rootMargin: '200px 0px 10% 0px', threshold: 0 });
    revealables.forEach(function (el) { ro.observe(el); });
  }

  /* ------------------------------------------------------ trace draw */
  $$('.draw').forEach(function (svg) {
    var strokes = $$('path, polyline, line, polygon', svg);
    strokes.forEach(function (el) {
      if (typeof el.getTotalLength !== 'function') return;
      var len = Math.ceil(el.getTotalLength());
      if (len) el.style.setProperty('--len', len);
    });
    if (reduced || !('IntersectionObserver' in window)) { svg.classList.add('is-drawn'); return; }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-drawn');
        io.unobserve(entry.target);
      });
    }, { threshold: 0.2 });
    io.observe(svg);
  });

  /* --------------------------------------------------------- overlap
     Standard time, no DST. A 09:00-18:00 day assumed on both sides.
       UK  London  09-18 GMT     = 09:00-18:00 UTC
           Hyderabad 13:30-22:30 IST (+5:30) = 08:00-17:00 UTC -> 8 h
       US  New York 09-18 EST (-5) = 14:00-23:00 UTC
           Hyderabad 15:30-00:00 IST = 10:00-18:30 UTC -> 4.5 h
       AU  Sydney  09-18 AEST (+10) = 23:00-08:00 UTC (wraps)
           Cebu    09-18 PHT  (+8)  = 01:00-10:00 UTC -> 7 h              */
  var MARKETS = {
    uk: {
      client: { city: 'London',   local: '09:00–18:00 GMT', bars: [[9, 18]] },
      team:   { city: 'Hyderabad', local: '13:30–22:30 IST', bars: [[8, 17]] },
      shared: { bars: [[9, 17]], hrs: '8 hours', utc: '09:00–17:00 UTC' }
    },
    us: {
      client: { city: 'New York',  local: '09:00–18:00 EST', bars: [[14, 23]] },
      team:   { city: 'Hyderabad', local: '15:30–00:00 IST', bars: [[10, 18.5]] },
      shared: { bars: [[14, 18.5]], hrs: '4.5 hours', utc: '14:00–18:30 UTC' }
    },
    au: {
      client: { city: 'Sydney', local: '09:00–18:00 AEST', bars: [[23, 24], [0, 8]] },
      team:   { city: 'Cebu',   local: '09:00–18:00 PHT',  bars: [[1, 10]] },
      shared: { bars: [[1, 8]], hrs: '7 hours', utc: '01:00–08:00 UTC' }
    }
  };

  var ovlTabs = $$('.market [data-market]');
  if (ovlTabs.length) {
    var tracks = {
      client: $('#ovlClientTrack'), team: $('#ovlTeamTrack'), shared: $('#ovlSharedTrack')
    };

    var paint = function (track, bars, cls, label) {
      if (!track) return;
      track.textContent = '';
      bars.forEach(function (range) {
        var bar = document.createElement('span');
        bar.className = 'bar ' + cls;
        bar.style.setProperty('--s', range[0]);
        bar.style.setProperty('--e', range[1]);
        if (label) bar.setAttribute('data-hrs', label);
        track.appendChild(bar);
      });
    };

    var render = function (key) {
      var m = MARKETS[key];
      if (!m) return;
      $('#ovlClientCity').textContent = m.client.city;
      $('#ovlClientHrs').textContent  = m.client.local;
      $('#ovlTeamCity').textContent   = m.team.city;
      $('#ovlTeamHrs').textContent    = m.team.local;
      $('#ovlSharedHrs').textContent  = m.shared.utc;
      paint(tracks.client, m.client.bars, 'bar-client');
      paint(tracks.team,   m.team.bars,   'bar-team');
      paint(tracks.shared, m.shared.bars, 'bar-shared', m.shared.hrs);
    };

    ovlTabs.forEach(function (tab, i) {
      tab.addEventListener('click', function () {
        ovlTabs.forEach(function (t) { t.setAttribute('aria-selected', 'false'); });
        tab.setAttribute('aria-selected', 'true');
        render(tab.getAttribute('data-market'));
      });
      tab.addEventListener('keydown', function (e) {
        var next = e.key === 'ArrowRight' ? i + 1 : e.key === 'ArrowLeft' ? i - 1 : -1;
        if (next < 0 || next >= ovlTabs.length) return;
        e.preventDefault();
        ovlTabs[next].focus();
        ovlTabs[next].click();
      });
    });
    render('uk');
  }

  /* -------------------------------------------------------- accordion */
  $$('[data-accordion] button[aria-controls]').forEach(function (btn) {
    var panel = document.getElementById(btn.getAttribute('aria-controls'));
    if (!panel) return;
    btn.addEventListener('click', function () {
      var open = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', String(!open));
      panel.hidden = open;
    });
  });

  /* ----------------------------------------------------- cookie banner */
  var KEY = 'optiserv.cookie.v1';
  var banner = $('#cookie');
  if (banner) {
    var stored = null;
    try { stored = localStorage.getItem(KEY); } catch (err) { stored = 'skip'; }
    if (!stored) {
      banner.hidden = false;
      $$('[data-cookie]', banner).forEach(function (btn) {
        btn.addEventListener('click', function () {
          try { localStorage.setItem(KEY, btn.getAttribute('data-cookie')); } catch (err) {}
          banner.hidden = true;
          /* Analytics slot — load tags here only when the value is "accept". */
        });
      });
    }
  }

  /* ------------------------------------------------------------- form */
  var form = $('#enquiry');
  if (form) {
    var summary = $('#formErrors');
    var status  = $('#formStatus');

    var problem = function (field) {
      if (field.validity.valueMissing)  return (field.getAttribute('data-label') || 'This field') + ' is required.';
      if (field.validity.typeMismatch && field.type === 'email') return 'Enter an email address in the form name@company.com.';
      if (field.validity.tooShort) return 'Please give us a little more detail — at least ' + field.minLength + ' characters.';
      return field.validationMessage;
    };

    var mark = function (field) {
      var slot = document.getElementById(field.id + '-err');
      var ok = field.checkValidity();
      field.setAttribute('aria-invalid', ok ? 'false' : 'true');
      if (slot) slot.textContent = ok ? '' : problem(field);
      return ok;
    };

    var fields = $$('input, textarea, select', form).filter(function (f) { return f.type !== 'hidden' && f.willValidate; });
    fields.forEach(function (field) {
      field.addEventListener('blur', function () { mark(field); });
      field.addEventListener('input', function () {
        if (field.getAttribute('aria-invalid') === 'true') mark(field);
      });
    });

    form.addEventListener('submit', function (e) {
      var bad = fields.filter(function (field) { return !mark(field); });
      if (!bad.length) {
        if (!form.getAttribute('action')) {
          /* No endpoint wired yet — do not pretend the message was sent. */
          e.preventDefault();
          if (status) {
            status.hidden = false;
            status.className = 'form-status is-warn';
            status.textContent = 'This form has no endpoint connected yet. Email sunil.s@optiservconsulting.com and we will pick it up there.';
          }
          return;
        }
        if (status) {
          status.hidden = false;
          status.className = 'form-status is-ok';
          status.textContent = 'Sending…';
        }
        form.querySelector('[type="submit"]').disabled = true;
        return;
      }
      e.preventDefault();
      if (summary) {
        summary.hidden = false;
        summary.textContent = bad.length === 1
          ? 'One field needs attention before we can send this.'
          : bad.length + ' fields need attention before we can send this.';
      }
      bad[0].focus();
    });
  }

  /* ------------------------------------------------- current page link */
  var here = location.pathname.split('/').pop() || 'index.html';
  $$('.nav a, .dropdown a').forEach(function (a) {
    if (a.getAttribute('href') === here) a.setAttribute('aria-current', 'page');
  });
})();
