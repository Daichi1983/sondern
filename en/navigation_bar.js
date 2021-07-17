﻿document.write('<nav class="navbar navbar-expand-lg navbar-light bg-info">');
document.write('<a class="navbar-brand text-light" href="/">Home</a>');
document.write('<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">');
document.write('<span class="navbar-toggler-icon"></span>');
document.write('</button>');
document.write('<div class="collapse navbar-collapse" id="navbarSupportedContent">');
document.write('<ul class="navbar-nav mr-auto">');
document.write('<li class="nav-item active">');
document.write('<a class="nav-link text-light" href="/ja/all-index.html">General Index of the Manuscript<span class="sr-only">(current)</span></a>');
document.write('</li>');
document.write('<li class="nav-item">');
document.write('<a class="nav-link text-light" href="/ja/sekiguchi.html">Who is Sekiguchi Tsugio?</a>');
document.write('</li>');
document.write('<li class="nav-item">');
document.write('<a class="nav-link text-light" href="/ja/about.html">About</a>');
document.write('</li>');
document.write('<li class="nav-item">');
document.write('<a class="nav-link text-light" href="/ja/inquiry.html">Inquiry</a>');
document.write('</li>');
document.write('<li class="nav-item">');
document.write('<a class="nav-link text-light disabled" href="#" tabindex="-1" aria-disabled="true">Links</a>');
document.write('</li>');
document.write('</ul>');
document.write('<button type="button" class="btn btn-outline-warning" onclick="lang_change()"><strong>JP</strong></button>');
document.write('<script type="text/javascript">');
document.write('function lang_change(){');
document.write('    var url= location.href;');
document.write('    var url= url.replace("/en/","/ja/");');
document.write('    location.href = url;');
document.write('}');
document.write('</script>');