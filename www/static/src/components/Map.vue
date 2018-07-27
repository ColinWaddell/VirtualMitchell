
<template>
  <div style="height: 600px">
    <div style="height: 10%; overflow: auto;">
      <h3>GeoJSON</h3>
      <label for="checkbox">GeoJSON Visibility</label>
      <input type="checkbox" id="checkbox" v-model="show">
      </br>
    </div>
    <l-map style="height: 90%" :zoom="zoom" :center="center">
      <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
      <l-geo-json v-if="show" :geojson="geojson" :options="options"></l-geo-json>
      <l-marker :lat-lng="marker"></l-marker>
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
            show: true,
            zoom: 13,
            center: [55.8642, -4.251],
            geojson: null,
            options: {
                style: function () {
                    return {
                        weight: 2,
                        color: 'red',
                        opacity: 1,
                        fillColor: '#e4ce7f',
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
    }
</script>