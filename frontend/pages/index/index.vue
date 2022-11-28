<template>
    <div class="col-span-3 mb-7 px-15">
      <div class="col-span-4 pageTitle">about</div>
      <p id="splashText"><span style="opacity:1">Hi there! My name is <b>Dexter</b> (he/him).</span><br /><br /><span style="opacity:0.8">I'm a <b>journalist</b>, a <b>programmer</b>, and a <b>designer</b>.</span><br /><br /><span style="opacity:0.5">I specialize in <b>data analysis</b> and <b>visualization</b>.</span></p><br><br>
      <p class="text-xl">I love Datawrapper, having created hundreds of audience-facing visualizations of everything from the war in Ukraine to interest rates. I've written <a href="https://github.com/dexmcmillan/datawrappergraphics" target="_blank"><b>a Python package</b></a> that makes it easy to chart your pandas dataframes in Datawrapper. I built this portfolio website using <b>Nuxt</b> and <b>Django</b>. I founded and ran a features publication for students called Paper Plane.</p><br>
      <p class="text-xl">Interested in hiring me? Click the tags on the left to toggle which skills you're interested in seeing on this page. Only those tags in dark blue will be shown.</p>
    </div>
  </template>
  
  <script>
  
  export default {
    name: "IndexPage",
    
  }
  </script>
  
  <style>
    

    #splashText b {
      border-bottom: 5px solid #2c3e50;
      padding-bottom:2px;
    }

  </style>
  