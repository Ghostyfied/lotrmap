<template>
			<div class="infoWindowWrapper">
				<div id="headerArea">
					<div id="headerIcon" onClick={this.props.handleCloseClickInfoBAr}>
						<FaBookOpen size="30px" />
					</div>
					<div class="infoHeader">
						<!-- {this.state.location} -->
					</div>
				</div>
				<div>
					<svg class="infoDivider" viewBox="0 0 600 120">
						<g id="layer1" transform="translate(-89.601 -425.81)">
							<g id="g2390">
							<g id="g2785" transform="matrix(.85040 0 0 .89861 12.065 46.69)">
								<path class="pathDivider" id="path2777" d="m439.25 460.28s0.01 26.32-35.96 18.74c-35.98-7.57-304.84-15.14-321.88 11.36 43.93-9.99 239.95-21.52 326.18-6.48 15.54 3.01 31.08 2.5 31.66-23.62z"/>
								<path class="pathDivider" id="path2783" d="m439.24 460.32s-0.01 26.32 35.96 18.75c35.97-7.58 304.83-15.15 321.87 11.36-43.92-10-239.94-21.53-326.17-6.49-15.54 3.01-31.09 2.51-31.66-23.62z"/>
							</g>
							<path class="pathDivider" id="path2813" d="m369.73 473.97c-1.57-8.79-3.55-15.44-11.94-16.01-8.38-0.57 5.43 4.44 11.94 16.01z"/>
							<path class="pathDivider" id="path2815" d="m373.38 462.92c-1.57-8.79-3.55-15.45-11.93-16.02-8.39-0.57 5.43 4.45 11.93 16.02z"/>
							<path class="pathDivider" id="path2817" d="m401.1 473.21c1.57-8.79 3.54-15.44 11.93-16.02 8.38-0.57-5.43 4.45-11.93 16.02z"/>
							<path class="pathDivider" id="path2819" d="m397.44 462.15c1.57-8.79 3.55-15.44 11.93-16.01 8.39-0.57-5.42 4.44-11.93 16.01z"/>
							<path class="pathDivider" id="path2823" d="m371.54 426.65s28.58 9.53-2.04 10.21c0 0 15.65-1.71 15.99 15.99 0-16.67 14.98-17.01 14.98-17.01-30.63 1.36-0.35-9.19-0.35-9.19l0.69-0.34-29.27 0.34z"/>
							<path class="pathDivider" id="path2829" d="m80.735 487.28c-14.61-18.84 36.135-20.76 40.365-22.3 4.23-1.53 9.23-4.23 1.54-12.3 21.91 8.07 103.8 14.61 103.8 14.61-41.13-1.15-145.7 4.23-145.7 19.99z"/>
							<path class="pathDivider" id="path2831" d="m690.58 486.59c14.61-18.83-36.14-20.76-40.37-22.29-4.23-1.54-9.22-4.23-1.54-12.31-21.91 8.08-103.8 14.61-103.8 14.61 41.14-1.15 145.71 4.23 145.71 19.99z"/>
							</g>
						</g>
					</svg>
				</div>
				<div class="infoBody">
					<!-- <Information location={this.state.location}/> -->
				</div>
			</div>
  </template>
  
  <script>
  export default {
    name: 'SideBar',
    data() {
      return {
        // Sidebar state
      };
    },
    methods: {
      // Sidebar methods
    }
  };
  </script>
  
  <style scoped lang="scss" src="../styles/SideBar.scss"></style>