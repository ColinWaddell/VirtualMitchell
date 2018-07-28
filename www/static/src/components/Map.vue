
<template>
  <div class="map">
    <div style="height: 450px">
        <l-map style="height: 90%; border-radius: 0.25rem;" :zoom="zoom" :center="center" ref="map">
            <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
            <l-geo-json :geojson="geojson" :options="options" @click="load_place" ref="geojson"></l-geo-json>
        </l-map>
    </div>
    <div v-if="records">
        <h4>{{ records.length }} Record<span v-if="records.length > 1">s</span>:</h4>
        <table class="table records">
            <thead class="thead-default">
                <tr>
                    <th></th>
                    <th>Description</th>
                    <th>Address</th>
                    <th>Date</th>
                    <th>Tags</th>
                </tr>
            </thead>
            <tbody>
                <tr 
                    scope="row" 
                    v-for="(record, index) in records"
                    :item="record"
                    :index="index"
                    :key="record.record_number"
                >
                    <td width="250" style="
                        background: white;
                        padding: 10px;
                        margin: 0;
                    ">
                        <div class="record-thumbnail">
                            <a 
                                :href="baseurl + record.image_url"
                                target="_blank"
                                class="record-thumbnail-img"
                                data-lightbox="previews"
                                :style="{ 
                                    backgroundImage: 'url(' + baseurl + record.image_url + ')',
                                    backgroundSize: 'cover'
                                }"
                                :data-title="get_title(record)"
                            ></a>
                            <a :if="record.caption" :href="image_url" class="image-caption">{{ record.caption }}</a>
                        </div>
                    </td>
                    <td>{{ record.description }}</td>
                    <td width="300" style="white-space: pre;">{{ get_address(record) }}</td>
                    <td width="150">{{ record.date_raw }}</td>
                    <td width="200">
                        <a
                            v-for="(tag, index) in record.tags"
                            :href="'?records__tags=' + tag"
                            :item="tag"
                            :index="index"
                            :key="tag"
                        >{{ tag }}<span v-if="index !== record.tags.length - 1">, </span></a>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
    <div v-else class="alert alert-info" role="alert">
        Select something from the map
    </div>
  </div>
</template>

<script>
    import { LMap, LTileLayer, LGeoJson, LMarker } from 'vue2-leaflet';
    import axios from 'axios';

    function onEachFeature(feature, layer) {
        let popupContent = Vue.extend(PopupContent);
        let popup = new popupContent({ propsData: { type: feature.geometry.type, text: feature.properties.popupContent }});
        layer.bindPopup(popup.$mount().$el);
    }
    
    export default {
        name: 'vmmap',

        components: {
            LMap,
            LTileLayer,
            LGeoJson,
            LMarker
        },

        data () {
            return {
                zoom: 13,
                center: [55.8642, -4.251],
                geojson: locations,
                records: null,
                baseurl: "http://www.mitchelllibrary.org/virtualmitchell/",
                options: {
                    style: function () {
                        return {
                            weight: 4,
                            color: '#e83e8c',
                            opacity: 1,
                            fillColor: '#e83e8c',
                            fillOpacity: 1,
                        }
                    },
                },
                url:'http://{s}.tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png',
                attribution:'&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
            }
        },

        mounted() {
            window.setTimeout(() => {
                this.resize_to_fit();
                if (this.geojson.length == 1){
                    console.log('ads')
                    this.load_records_url(this.geojson[0].properties.record_request_url);
                }
            }, 0);
        },

        methods: {
            load_place: function (event) {
                let records_url = event.layer.feature.properties.record_request_url;
                this.load_records_url(records_url);
            },

            load_records_url: function(records_url) {
                axios.get(records_url).then(response => {
                    this.records = response.data;
                });
            },

            resize_to_fit: function(event) {
                if (this.$refs.geojson && this.$refs.geojson.getBounds){
                    this.$refs.map.fitBounds(
                        this.$refs.geojson.getBounds(),
                        {animate: true}
                    );
                }
            },

            get_address: function (record) {
                return `${record.number ? record.number + ', ' : ''}` + 
                       `${record.street ? record.street + '\n' : ''}` + 
                       `${record.area ? record.area : ''}`;
            },

            get_title: function(record) {
                return `${record.caption}` + 
                       `${record.description ? ' - ' + record.description : ''}` + 
                       `${record.date_raw ? ' - ' + record.date_raw : '' }`;
            }
        }
    }
</script>