<template>
  <div class="app">
    <!-- <Sidebar /> -->
    <div class="mapContainer">
      <SVGMap @click-location="handleClickLocation" />
    </div>
    <!-- <InfoBar v-if="barState" :location="location" @close-info-bar="handleCloseClickInfoBar" /> -->
  </div>
</template>

<script>
import Sidebar from './components/SideBar.vue';
import SVGMap from './components/SVGMap.vue';
import InfoBar from './components/InfoBar.vue';

export default {
  name: 'App',
  components: {
    Sidebar,
    SVGMap,
    InfoBar
  },
  data() {
    return {
      location: '',
      index: '',
      barState: false
    };
  },
  methods: {
    handleClickLocation(index, location) {
      this.location = location;
      this.index = index;
      if (!this.barState) {
        this.barState = true;
      }
    },
    handleCloseClickInfoBar() {
      this.barState = false;
    }
  }
};
</script>

<style lang="scss" src="./styles/Global.scss">

</style>