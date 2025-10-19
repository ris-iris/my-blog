---
title: A post about how I created this post
date: 2025-10-19
categories: coding
---

Ok, so I decided to start a blog. And I decided to use Github Pages for this purpose. This post is documenting my attempt at creating this post and the blog in general (and I find it quite funny).

## Initial setup
It's really easy, you just go to [the documentation](https://docs.github.com/en/pages/quickstart) and do what you are asked to do.
I additionally tried to add ``description`` field to my ``_config.yml`` to see what happens.

After this step, my newborn blog looked like this:
<img src="../images/my_blog_screenshot_2025-10-19_13:30.png"/>

<details>
    <summary>A side note on HTML markups</summary>
    <p>To add an image to the post, you can:</p>
    <ol>
    <li>Create a folder <code>images</code> in the repo and add an image there</li>
    <li>Add an image with <code>&lt;img src=&quot;relative-path-to-images/your-image-file&quot;/&gt;</code></li>
    </ol>
    <p>To create a toggle use:</p>
    <pre><code>`<span class="javascript"></span>``<span class="javascript">
    &lt;details&gt;
      <span class="xml"><span class="hljs-tag">&lt;<span class="hljs-name">summary</span>&gt;</span>A side note on HTML markups<span class="hljs-tag">&lt;/<span class="hljs-name">summary</span>&gt;</span></span>
      And here is how you <span class="hljs-keyword">do</span> it
    &lt;<span class="hljs-regexp">/details&gt;
    </span></span>``<span class="javascript"><span class="hljs-regexp"></span></span>`
    </code></pre>
  <p>And, apparently, you can not use markdown inside the markup part, so if you are not fluent in HTML, use a converter like this one: https://markdowntohtml.com/</p>
</details>

## Now, what do I do next
