---
title: A post about how I created this post
date: 2025-10-19
tags: github_pages
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

## Understand categories
I noticed in some of the examples I looked through, there were ``categories``, which seem useful for me, because I'm planning on logging all my various hobbies in here. So, turns out, you can create multiple folders and add ``_posts`` subfolder to automatically set categories for a post (this is the point where I move this file to a new folder). You don't have to, anyway the url of a post with a category will look like ``blog_url/category/post``

There are also ``tags``, which you can iterate over, but they are not included in the path to the post. This can be useful for more precise definition of the topics of the post, I guess...

I decided not to touch collections for now, because it seems I don't really need them.

## Make it pretty!
I can tolerate the font and the colors of my blog at this stage, but the "Home" title on the home page irritates me. So, we are going to change the layout. I browsed for a bit existing Jekyll themes, and will use the [minima layeout](https://github.com/jekyll/minima/tree/master/_layouts) to begin with. So, I just copy them, and then edit some things here and there.
