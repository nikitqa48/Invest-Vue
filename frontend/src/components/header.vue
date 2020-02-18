<template>
        <q-toolbar class="header text-white" >
      <q-separator dark vertical inset />
      <q-btn stretch flat label="Инвест Липецк" to = "/"/>
      <q-space />

      <q-btn-dropdown stretch flat label="Dropdown">
        <q-list>
          <q-item-label header>Folders</q-item-label>
          <q-item clickable v-close-popup tabindex="0">
            <q-item-section avatar>
              <q-avatar icon="folder" color="secondary" text-color="white" />
            </q-item-section>
            <q-item-section>
              <q-item-label>Photos</q-item-label>
              <q-item-label caption>February 22, 2016</q-item-label>
            </q-item-section>
            <q-item-section side>
              <q-icon name="info" />
            </q-item-section>
          </q-item>
          <q-separator inset spaced />
          <q-item-label header>Files</q-item-label>
          <q-item v-for="n in 3" :key="`y.${n}`" clickable v-close-popup tabindex="0">
            <q-item-section avatar>
              <q-avatar icon="assignment" color="primary" text-color="white" />
            </q-item-section>
            <q-item-section>
              <q-item-label>Vacation</q-item-label>
              <q-item-label caption>February 22, 2016</q-item-label>
            </q-item-section>
            <q-item-section side>
              <q-icon name="info" />
            </q-item-section>
          </q-item>
        </q-list>
      </q-btn-dropdown>
      <q-separator dark vertical />
      <q-btn stretch flat label="О НАС" />
      <q-separator dark vertical />
      <q-btn stretch flat label="РЕГИОН" />
       <q-separator dark vertical />
      <q-btn stretch flat label="УСЛУГИ" />
      <q-separator dark vertical />
      <q-btn stretch flat label="ИНВЕСТОРУ" />
      <q-separator dark vertical />
      <q-btn  to ='/state' stretch flat label="ГОСПОДДЕРЖКА" />
       <q-separator dark vertical />
       <q-btn stretch flat label="ПЛОЩАДКИ" />
       <q-separator dark vertical />
       <q-btn stretch flat label="ПРЕСС-ЦЕНТР" />
        <q-separator dark vertical />
        <q-btn stretch flat label="КОНТАКТЫ" />
    </q-toolbar>
</template>
<script>
export default {
    
}
</script>
<style scoped>
.header{
  font-size: 1vw;
  position: absolute;
  z-index: 1;
  background: #262626;
}
</style>