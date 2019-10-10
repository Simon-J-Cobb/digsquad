<template>
  <div class="page-container" style="min-height: 100vh; justify-content: center;">

    <md-app md-mode="reveal" style="min-height: 100vh;">

      <md-app-toolbar class="md-large md-dense md-primary">
        <div class="md-toolbar-row">
          <div class="md-toolbar-section-start">
            <md-button class="md-icon-button" @click="menuVisible = !menuVisible">
              <md-icon>menu</md-icon>
            </md-button>
            <span class="md-title">GreenHub</span>
          </div>
            <div class="md-toolbar-section-end">
              <md-button class="md-icon-button" @click="this.$router.go(0)">
                <md-icon>refresh</md-icon>
              </md-button>
            </div>
        </div>

        <div class="md-toolbar-row">
          <md-tabs class="md-primary">
            <md-tab id="tab-home" md-label="Donations" to="/donate-from"></md-tab>
            <md-tab id="tab-pages" md-label="Investments" to="/donate-to"></md-tab>
          </md-tabs>
        </div>
      </md-app-toolbar>

      <md-app-drawer :md-active.sync="menuVisible">
        <md-toolbar class="md-transparent" md-elevation="0">
          <md-avatar class="md-avatar-icon">
            <img src="@/assets/Logo3.png" alt="GreenHub">
          </md-avatar>
        </md-toolbar>

        <md-list>
          <md-list-item>
            <md-icon>dns</md-icon>
            <span class="md-list-item-text">Donations & Investments</span>
          </md-list-item>

          <md-list-item>
            <md-icon>settings_applications</md-icon>
            <span class="md-list-item-text">Confgure investments</span>
          </md-list-item>

          <md-list-item>
            <md-icon>account_box</md-icon>
            <span class="md-list-item-text">Account</span>
          </md-list-item>
        </md-list>
      </md-app-drawer>

      <md-app-content>
        <div style="padding: 50px; min-height: 100vh;">  
          <router-view></router-view> 
        </div>
      </md-app-content>

    </md-app>
  </div>
</template>

<style lang="scss" scoped>

//  @import '~vue-material/dist/theme/black-green-dark.css';
//@import '~vue-material/dist/theme/default-dark.css';

.md-app {
    padding: 0px;
    /*width: 650px;*/
    max-height: 400px;
    border: 1px solid rgba(#000, .12);
  }

   // Demo purposes only
  .md-drawer {
    padding: 0px;
    width: 300px;
    max-width: calc(100vw - 125px);
  }
</style>

<script>
export default {
  name: 'App',
  data: () => ({
    menuVisible: false
  })
}
</script>