<template>
    <div>
        <div class="row">
            <div class="col-3">
                <div class="input-group mb-3">
                    <input 
                        type="text"
                        class="form-control"
                        placeholder="Address Lookup"
                        aria-label="Address Lookup"
                        aria-describedby="button-addon2"
                        v-model="search_term"
                    >
                    <div class="input-group-append">
                        <button class="btn btn-outline-secondary" type="button" @click="search_click">
                            <span class="glyphicon glyphicon-search"></span>
                        </button>
                    </div>
                </div>
            </div>
            <div class="col-9">
                <div class="map">
                    <div style="height: 450px">
                        <l-map style="height: 90%; border-radius: 0.25rem;" :zoom="zoom" :center="center" ref="rl_map">
                            <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
                            <l-geo-json :geojson="geojson" :options="options" ref="rl_geojson"></l-geo-json>
                        </l-map>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import { LMap, LTileLayer, LGeoJson, LMarker } from 'vue2-leaflet';
    import axios from 'axios';
    
    export default {
        name: 'vmrecordlocation',

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
                geojson: [],
                records: null,
                display_name: null,
                place_id: null,
                baseurl: "http://www.mitchelllibrary.org/virtualmitchell/",
                options: {
                    style: function () {
                        return {
                            weight: 4,
                            color: '#e83e8c',
                            opacity: 0.7,
                            fillColor: '#e83e8c',
                            fillOpacity: 0.2,
                        }
                    },
                },
                url:'http://{s}.tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png',
                attribution:'&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
            }
        },

        mounted() {
            window.setTimeout(() => {
                // this.resize_to_fit();
                // if (this.geojson.length == 1){
                //     console.log('ads')
                //     this.load_records_url(this.geojson[0].properties.record_request_url);
                // }
            }, 0);
        },

        methods: {
            search_click: function(event) {
                console.log('yo')
            },
        //     load_place: function (event) {
        //         let records_url = event.layer.feature.properties.record_request_url;
        //         let display_name = event.layer.feature.properties.display_name;
        //         this.place_id = event.layer.feature.properties.place_id;

        //         this.load_records_url(records_url, display_name);
        //         // this.jump_to_spot(event.latlng); // needs work
        //     },

        //     load_records_url: function(records_url, display_name) {
        //         axios.get(records_url).then(response => {
        //             this.records = response.data;
        //             this.display_name = display_name
        //         });
        //     },

        //     jump_to_spot: function(latlng){
        //         var corner1 = L.latLng(latlng.lat-0.01, latlng.lng-0.01)
        //         let corner2 = L.latLng(latlng.lat+0.01, latlng.lng+0.01)
        //         let bounds = L.latLngBounds(corner1, corner2);
        //         this.$refs.map.setBounds(bounds)
        //     },

        //     resize_to_fit: function(event) {
        //         if (this.$refs.geojson && this.$refs.geojson.getBounds){
        //             this.$refs.map.fitBounds(
        //                 this.$refs.geojson.getBounds(),
        //                 {animate: true}
        //             );
        //         }
        //     },

        }
    }
</script>