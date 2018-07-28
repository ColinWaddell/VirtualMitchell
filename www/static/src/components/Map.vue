
<template>
  <div class="map">
    <div style="height: 450px">
        <l-map style="height: 90%" :zoom="zoom" :center="center">
        <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
        <l-geo-json :geojson="geojson" :options="options" @click="load_place"></l-geo-json>
        </l-map>
    </div>
    <table class="table records" v-if="records">
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
                <td>{{ caption }}</td>
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
</template>

<script>
    import { LMap, LTileLayer, LGeoJson, LMarker } from 'vue2-leaflet';
    import axios from 'axios';
    
    export default {
        name: 'example',
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
                geojson: null,
                records: null,
                baseurl: "http://www.mitchelllibrary.org/virtualmitchell/",
                options: {
                    style: function () {
                        return {
                            weight: 2,
                            color: '#e83e8c',
                            opacity: 1,
                            fillColor: '#e83e8c',
                            fillOpacity: 1
                        }
                    }
                },
                url:'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
                attribution:'&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
            }
        },
        created () {
            this.geojson = locations;
        },
        methods: {
            load_place: function (event) {
                let records_url = event.layer.feature.properties.record_request_url;
                axios.get(records_url).then(response => {
                    this.records = response.data;
                });
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