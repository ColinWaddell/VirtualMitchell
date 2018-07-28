
<template>
  <div style="height: 600px">
    <l-map style="height: 90%" :zoom="zoom" :center="center">
      <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
      <l-geo-json :geojson="geojson" :options="options" @click="load_place"></l-geo-json>
    </l-map>
  </div>
</template>

<script>
    import { LMap, LTileLayer, LGeoJson, LMarker } from 'vue2-leaflet';
    
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
                let place_id = event.layer.feature.properties.record_request_url;
                console.log(place_id)
            }
        }
    }
</script>