<template>
  <div class="right_wrapper">
              <div class="data_region">
                <div class="invest_wrapper">
                  <h2 class="invest" v-if="region[index].region == '1'">Данков</h2>
                  <h2 class="invest" v-if="region[index].region == '2'">Лев Толстой</h2>
                  <h2 class="invest" v-if="region[index].region == '3'">Чаплыгин</h2>
                  <h2 class="invest" v-if="region[index].region == '6'">Лебедянь</h2>
                  <h2 class="invest" v-if="region[index].region == '7'">Доброе</h2>
                  <span class="border_invest"></span>
                </div>
                <div class="wrapper_data">
                  <div class="left">
                    <div class="grinfield">
                      <q-card class="noname">
                        <q-tabs
                          class="text-grey-6"
                          v-model="tab"
                          dense
                          dark
                          active-color="grey-1"
                          indicator-color="grey-5"
                          align="justify"
                        >
                          <q-tab name="logic" label="Логистика" />
                          <q-tab name="institute" label="Институты" />
                          <q-tab name="greenfield" label="Гринфилд" />
                          <q-tab name="brownfield" label="Браунфилд" />
                        </q-tabs>
                        <q-separator />
                        <q-tab-panels v-model="tab" animated style="min-height: 50%">
                          <q-tab-panel name="greenfield" class="text-grey-2">
                            <q-splitter v-model="splitterModel">
                              <template v-slot:before>
                                <q-tabs
                                  v-model="innerTab"
                                  vertical
                                  style="max-width: 100%"
                                  class="text-grey-2"
                                >
                                  <q-tab name="greenfield" label="Что это такое?" class="qtab" />
                                  <q-tab
                                    name="greenfield1"
                                    label="S: 12.3 га 71:12:050211:141"
                                    v-if="index == 1"
                                  />
                                  <q-tab
                                    name="greenfield2"
                                    label="S: 12.3 га 71:12:333"
                                    v-if="index == 2"
                                  />
                                </q-tabs>
                              </template>

                              <template v-slot:after>
                                <q-tab-panels
                                  v-model="innerTab"
                                  class="text-grey-5"
                                  animated
                                  transition-prev="slide-down"
                                  transition-next="slide-up"
                                >
                                  <q-tab-panel name="greenfield">
                                    <div class="text-h4 q-mb-md">Описание</div>
                                    <p class="text-p5">
                                      Индустриальный (промышленный) парк – это управляемый единым оператором (специализированной управляющей компанией) комплекс объектов недвижимости, состоящий из земельного участка (участков) с производственными, административными, складскими и иными помещениями и сооружениями, обеспеченный энергоносителями, инженерной и транспортной инфраструктурой и административно-правовыми условиями для размещения производств.
                                      Понятия «индустриальный парк» и «промышленный парк» тождественны.
                                      Основные типы индустриальных (промышленных) парков:
                                      1) гринфилд (greenfield);
                                      2) браунфилд (brownfield).
                                      Индустриальный парк типа «гринфилд» (greenfield) - индустриальный (промышленный) парк, создаваемый на вновь отведенном незастроенном земельном участке, как правило, изначально не обеспеченном инфраструктурой.
                                    </p>
                                  </q-tab-panel>

                                  <q-tab-panel name="greenfield1" v-if="index == 0">
                                    <div class="text-h4 q-mb-md">S: 5.3 га 71:23:070220:1711</div>
                                    <div class="text-grey-2">
                                      <img
                                        ref="grinf"
                                        src="../statics/image/acb4a7b1e50838f4079c799b14cf606c.jpg"
                                        class="grinf"
                                        @click="modalImage"
                                      />
                                    </div>
                                  </q-tab-panel>

                                  <q-tab-panel name="greenfield1" v-if="index == 1">
                                    <div class="text-h4 q-mb-md">S: 5.3 га 71:23:070220:17</div>
                                    <img
                                      src="../statics/image/acb4a7b1e50838f4079c799b14cf606c.jpg"
                                      ref="grinf"
                                      @click="modalImage"
                                      class="grinf"
                                    />
                                  </q-tab-panel>
                                  <q-tab-panel name="greenfield2" v-if="index == 2">
                                    <div class="text-h4 q-mb-md">гринфилд 2</div>
                                    <img
                                      src="../statics/image/acb4a7b1e50838f4079c799b14cf606c.jpg"
                                      ref="grinf"
                                      @click="modalImage"
                                      class="grinf"
                                    />
                                  </q-tab-panel>
                                </q-tab-panels>
                              </template>
                            </q-splitter>
                          </q-tab-panel>

                          <q-tab-panel name="brownfield">
                            <q-splitter v-model="splitterModel">
                              <template v-slot:before>
                                <q-tabs
                                  v-model="brownfield"
                                  vertical
                                  style="max-width: 100%"
                                  class="text-grey-2"
                                >
                                  <q-tab
                                    name="brownfield"
                                    label="S: 5.3 га 71:23:070220:17"
                                    class="qtab"
                                    v-if="index == 0"
                                  />
                                  <q-tab
                                    name="brownfield1"
                                    label="S: 12.3 га 71:12:050211:141"
                                    v-if="index == 0"
                                  />
                                  <q-tab
                                    name="brownfield2"
                                    label="S: 12.3 га 71:12:333"
                                    v-if="index == 1"
                                  />
                                </q-tabs>
                              </template>

                              <template v-slot:after>
                                <q-tab-panels
                                  v-model="brownfield"
                                  class="text-grey-5"
                                  animated
                                  transition-prev="slide-down"
                                  transition-next="slide-up"
                                >
                                  <q-tab-panel name="brownfield">
                                    <div class="text-h4 q-mb-md">1</div>
                                    <div class="text-grey-2">
                                      <img
                                        src="../statics/image/acb4a7b1e50838f4079c799b14cf606c.jpg"
                                        class="grinf"
                                      />
                                    </div>
                                  </q-tab-panel>

                                  <q-tab-panel name="brownfield1" v-if="index == 0">
                                    <div class="text-h4 q-mb-md">S: 5.3 га 71:23:070220:17</div>
                                    <img
                                      src="../statics/image/acb4a7b1e50838f4079c799b14cf606c.jpg"
                                      class="grinf"
                                    />
                                  </q-tab-panel>
                                  <q-tab-panel name="brownfield2" v-if="index == 1" animated>
                                    <div class="text-h4 q-mb-md">2</div>
                                    <img
                                      src="../statics/image/acb4a7b1e50838f4079c799b14cf606c.jpg"
                                      class="grinf"
                                    />
                                  </q-tab-panel>
                                </q-tab-panels>
                              </template>
                            </q-splitter>
                          </q-tab-panel>
                          <q-tab-panel name="logic">
                            <div class="logic">
                              <div class="data1">
                                <div class="data_inside">
                                  <p class="p_region">
                                    <span class="number">{{region[index].power}}</span>
                                    МВт
                                  </p>
                                  <p class="territory">электроснабжение</p>
                                </div>
                                <div class="data_inside">
                                  <p class="p_region">
                                    <span class="number">{{region[index].water_out}}</span>
                                    тыс.куб м/сут
                                  </p>
                                  <p class="territory">Водоотведение</p>
                                </div>
                              </div>
                              <div class="data2">
                                <div class="data_inside">
                                  <p class="p_region">
                                    <span class="number">{{region[index].water}}</span>
                                    тыс. куб м/сут
                                  </p>
                                  <p class="territory">Водоснабжение</p>
                                </div>
                                <div class="data_inside">
                                  <p class="p_region">
                                    <span class="number">{{region[index].gas}}</span>
                                    тыс. куб м/сут
                                  </p>
                                  <p class="territory">Газоснабжение</p>
                                </div>
                              </div>
                            </div>
                            <div class="data_inside">
                              <p class="p_region">
                                <span class="number">{{region[index].heat}}</span>
                                Гкал/час
                              </p>
                              <p class="territory">Теплоснабжение</p>
                            </div>
                          </q-tab-panel>
                          <q-tab-panel name="institute">
                            <ul class="institutes">
                              <li
                                class="dolgorukogo"
                                id="inst1map"
                                @mouseover="showInstitute"
                                @mouseleave="hideInstitute"
                              >1 Институт</li>
                              <li
                                class="dobroe"
                                @mouseover="showInstitute"
                                @mouseleave="hideInstitute"
                              >2 Институт</li>
                              <li
                                class="stanovoe"
                                @mouseover="showInstitute"
                                @mouseleave="hideInstitute"
                              >3 Институт</li>
                              <li
                                class="elec"
                                @mouseover="showInstitute"
                                @mouseleave="hideInstitute"
                              >4 Институт</li>
                            </ul>
                          </q-tab-panel>
                        </q-tab-panels>
                      </q-card>
                    </div>
                  </div>
                </div>
              </div>
              </div>
            </div>
</template>
