<template>
  <svg version="1.1" id="svg_frame" baseProfile="tiny" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3600 2400" width="100%" height="100%" xmlSpace="preserve">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Gabriola">
    <Arrows />
    <Bridges />
    <Cities />
    <Coastline />
    <Display_font />
    <Lakes />
    <Legend />
    <Mountains_and_forests />
    <Other_font />
    <Rivers />
    <Streets />
  </svg>
</template>
  
<script>
import Arrows from '@/SVGs/Arrows.vue';
import Bridges from '@/SVGs/Bridges.vue';
import Cities from '@/SVGs/Cities.vue';
import Coastline from '@/SVGs/Coastline.vue';
import Display_font from '@/SVGs/Display_font.vue';
import Lakes from '@/SVGs/Lakes.vue';
import Legend from '@/SVGs/Legend.vue';
import Mountains_and_forests from '@/SVGs/Mountains_and_forests.vue';
import Other_font from '@/SVGs/Other_font.vue';
import Rivers from '@/SVGs/Rivers.vue';
import Streets from '@/SVGs/Streets.vue';

export default {
  name: 'SVGMap',
  props: ['handleClickLocation'],
  components: {
    Arrows,
    Bridges,
    Cities,
    Coastline,
    Display_font,
    Lakes,
    Legend,
    Mountains_and_forests,
    Other_font,
    Rivers,
    Streets,
    Arrows
},
  mounted() {
    // Logic for handling SVG interactions
  }
};
</script>
  
<style scoped lang="scss" src="../styles/SVGMap.scss"></style>