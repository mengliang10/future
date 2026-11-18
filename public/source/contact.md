---
layout: page
title: Contact
subtitle: Research inquiries, partnership opportunities, and feedback.
permalink: /contact/
---

Whether you have a question about the analysis, want to discuss a research partnership, or have feedback on the site: reach out.

<!-- Formspree form: replace ACTION_URL with your Formspree endpoint after signing up at formspree.io -->
<form class="contact-form" action="https://formspree.io/f/REPLACE_WITH_YOUR_FORM_ID" method="POST">

  <div class="form-group">
    <label class="form-label" for="name">Name</label>
    <input class="form-input" type="text" id="name" name="name" placeholder="Your name" required>
  </div>

  <div class="form-group">
    <label class="form-label" for="email">Email</label>
    <input class="form-input" type="email" id="email" name="email" placeholder="you@example.com" required>
  </div>

  <div class="form-group">
    <label class="form-label" for="subject">Subject</label>
    <select class="form-select" id="subject" name="subject">
      <option value="general">General Inquiry</option>
      <option value="research">Research / Partnership</option>
      <option value="advertising">Advertising / Sponsorship</option>
      <option value="feedback">Site Feedback</option>
      <option value="other">Other</option>
    </select>
  </div>

  <div class="form-group">
    <label class="form-label" for="message">Message</label>
    <textarea class="form-textarea" id="message" name="message" placeholder="Your message..." required></textarea>
  </div>

  <button type="submit" class="btn btn-primary">Send Message</button>

</form>

<div class="callout callout-info" style="margin-top:1.5rem;">
  <span class="callout-icon">&#9432;</span>
  <span>Powered by <strong>Formspree</strong>: free for basic use, no server required. Sign up at <a href="https://formspree.io" target="_blank">formspree.io</a> and replace the form action URL above with your endpoint.</span>
</div>
