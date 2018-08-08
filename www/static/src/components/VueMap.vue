<template>
        <l-map style="height: 90%; border-radius: 0.25rem;" :zoom="zoom" :center="center" ref="map">
            <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
            <l-geo-json :geojson="geojson" :options="options" @click="clickhandler" ref="geojson"></l-geo-json>
        </l-map>
</template>

<script>
    import { LMap, LTileLayer, LGeoJson, LMarker } from 'vue2-leaflet';

    function onEachFeature(feature, layer) {
        let popupContent = Vue.extend(PopupContent);
        let popup = new popupContent({ propsData: { type: feature.geometry.type, text: feature.properties.popupContent }});
        layer.bindPopup(popup.$mount().$el);
    }
    
    export default {
        name: 'vuemap',

        components: {
            LMap,
            LTileLayer,
            LGeoJson,
            LMarker
        },

        props: ['clickhandler', 'geojson'],

        data () {
            return {
                zoom: 13,
                center: [55.8642, -4.251],
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

        },

        methods: {

            jump_to_spot: function(latlng){
                var corner1 = L.latLng(latlng.lat-0.01, latlng.lng-0.01)
                let corner2 = L.latLng(latlng.lat+0.01, latlng.lng+0.01)
                let bounds = L.latLngBounds(corner1, corner2);
                this.$refs.map.setBounds(bounds)
            },

            resize_to_fit: function(event) {
                window.setTimeout(() => {
                    if (this.$refs.geojson && this.$refs.geojson.getBounds){
                        this.$refs.map.fitBounds(
                            this.$refs.geojson.getBounds(),
                            {animate: true}
                        );
                    }
                }, 0);
            },

            load_records: function(records) {
                this.records = records;
            }
        }
    }
</script>