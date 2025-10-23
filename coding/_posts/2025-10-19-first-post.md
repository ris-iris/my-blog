---
title: A post about this post creation
date: 2025-10-19
tags: github_pages
image: /my-blog/coding/images/my_blog_screenshot_2025-10-19_13:30.png
---

Ok, so I decided to start a blog. And I decided to use Github Pages for this purpose. This post is documenting my attempt at creating this post and the blog in general (and I find it quite funny).

## Initial setup
It's really easy, you just go to [the documentation](https://docs.github.com/en/pages/quickstart) and do what you are asked to do.
I additionally tried to add ``description`` field to my ``_config.yml`` to see what happens.

After this step, my newborn blog looked like this:
<table style="width: 100%; table-layout: fixed; border-collapse: collapse; border: none;">
  <tr style="border: none;">
    <td style="width: 50%; padding: 10px; border-collapse: collapse; vertical-align: top; border: none;">
     <img src="/my-blog/coding/images/my_blog_screenshot_2025-10-19_13:30.png" />
    </td>
    <td style="width: 50%; padding: 10px; border-collapse: collapse; vertical-align: top; border: none;">
      <details>
            <summary>A side note on HTML markups</summary>
            <p>To add an image to the post, you can:</p>
            <ol>
            <li>Create a folder <code>images</code> in the repo and add an image there</li>
            <li>Add an image with <code>&lt;img src=&quot;path-to-images-from-the-root/your-image-file&quot;/&gt;</code></li>
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
    </td>
  </tr>
</table>

## Understand categories
I noticed in some of the examples I looked through, there were ``categories``, which seem useful for me, because I'm planning on logging all my various hobbies in here. So, turns out, you can create multiple folders and add ``_posts`` subfolder to automatically set categories for a post (this is the point where I move this file to a new folder). You don't have to, anyway the url of a post with a category will look like ``blog_url/category/post``

There are also ``tags``, which you can iterate over, but they are not included in the path to the post. This can be useful for more precise definition of the topics of the post, I guess...

I decided not to touch collections for now, because it seems I don't really need them.

Another thing I noticed at this point, is that the path to the post is quite long with the year, month and date before the name of the post, which I didn't particularly like. To just output the path like `category/post-title`, I set the permalink attribute in the `_config.yml` to `permalink: none`.

Generally, I would advise you to check out [the config of minima theme](https://github.com/jekyll/minima/blob/master/_config.yml), it has enough comments to make sense of what is happening.

## Make it pretty!
I can tolerate font, colors, and all other questionable design choises of my blog at this stage, but the "Home" title on the home page irritates me so much. So, we are going to change the layout. I browsed existing Jekyll themes for a bit, and will use the [minima layouts](https://github.com/jekyll/minima/tree/master/_layouts) to begin with. So, as any good programmer, I just copy them, and then edit some things here and there...

... important note, when you copy the theme `_layouts` and `_includes`, don't forget to copy `_sass` and `assets` as well (otherwise the result will look quite ugly, but I'm not judging if it's what you were going for).

And, allow me to present a [piece of code](https://github.com/ris-iris/my-blog/blob/c7946fe79f55026db08954b93119e531382b6b28/_includes/nav-items.html) I'm proud of, that creates a dropdown for categories in the navigation bar (it goes into `_includes/nav-items` right after the list of `nav-item`-s):

At this point I figured out I need to add the dropdown style to `_sass/minima/custop-styles.scss`, but look at this slight mismatch: <img src="/my-blog/coding/images/my_blog_screenshot_2025-10-20.png" />, and it took me quite a lot of trial and error to figure out the combination of parameters for the styles, that will even thing out. So, maybe I should have learned a bit of css before copypasting things... Anyways, it worked in the end!

### Make it even prettier
I have some visually heavy projects in mind, and when I saw the [wind theme](https://github.com/a-chacon/wind/tree/main), I knew I want a galery of posts with nice thumbnail pictures too.
And turns out that I just need an image grid for that, sound quite simple, right? Based on [this tutorial](https://www.w3schools.com/howto/howto_js_image_grid.asp), you just divide all the posts in columns and make the column style ``flex``. But how do you do it, if you need to iterate over all the posts you have? And here I gave up and went to Claude for answers about the wind layouts... It's not too complicated, but this time I want to understand what the css style is doing before I copy it.

## To sum up
If you want your blog as soon as possible, then maybe just choose a theme that you like, preferably the one with nice documentation, and copy it. If you prefere to get your hands dirty, then I would do the following:
1. Use Github Pages quickstart to get the initial setup done
2. Be prepared to use your residual markdown knowledge to it's fullest to create your home page and a post or two
   - If markdown isn't enough for your creative needs, just paste html right in the middle of your post, like I did here:
 
     <img src="/my-blog/coding/images/my_blog_screenshot_2025-10-20_20:30.png" />
3. Check out Jekyll docs to get a little more insight about [front matters](https://jekyllrb.com/docs/front-matter/) and [Liquid](https://jekyllrb.com/docs/liquid/) magic
4. Go through minima theme repo to get inspired and see some clear examples of the concepts you saw in the previous step
5. Copy `_includes`, `_layouts`, `_sass`, and `assets` to your project
6. Incarnate your wildest design fantasies in the layouts and don't forget to include the layout name in the front matters of the pages
7. \[TBD\] comments, SEO, and all the other cool thigs I skipped
8. Don't forget to squash all the commits, so no one sees how bad you were trying to figure out that one particular padding value


