---
layout: post
title: Make a multi-resolution favicon.ico from a source image, using ImageMagick
categories:
 - Favicon
date: 2016-01-15 01:27:00 +0000
---

convert favicon.png -define icon:auto-resize=64,48,32,16 favicon.ico