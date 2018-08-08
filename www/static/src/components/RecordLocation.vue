<template>
    <div>
        <div class="row">
            <div class="col-9">
                <div class="map">
                    <div style="height: 450px">
                        <vuemap :clickhandler="map_click" :geojson="geojson" ref="map"></vuemap>
                    </div>
                </div>
            </div>
            <div class="col-3">
                <div class="input-group mb-3">
                    <input 
                        type="text"
                        class="form-control"
                        placeholder="Address Lookup"
                        aria-label="Address Lookup"
                        aria-describedby="button-addon2"
                        v-model="search_term"
                        @keydown.enter="search_submit"
                    >
                    <div class="input-group-append">
                        <button class="btn btn-outline-secondary" type="button" @click="search_submit">
                            <span class="glyphicon glyphicon-search"></span>
                        </button>
                    </div>
                </div>

                <span class="badge badge-primary" v-if="!results && !search_term">Search for a location in Glasgow</span>
                <span class="badge badge-info" v-if="!results && search_term">Hit the search button</span>
                
                <h6 v-if="results && results.length">Select a result:</h6>
                <span 
                    v-if="results"
                    v-for="(result, index) in results"
                    :item="result"
                    :index="index"
                    :key="result.place_id"
                >
                    <button 
                        class="btn btn-outline-primary"
                        type="button"
                        @click="result_click(result)"
                        v-html="index + 1"
                    ></button>
                    <span> </span>
                </span>

                <span 
                    class="badge badge-warning"
                    v-if="results && results.length==0"
                    >Nothing found</span>

                <div v-if="selected">
                    <hr />
                    {{ selected.display_name }}
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    
    export default {
        name: 'vmrecordlocation',

        data () {
            return {
                search_term: '',
                results: null,
                selected: null,
                geojson: [],
            }
        },

        mounted() {

        },

        methods: {
            build_search_url(lookup){
                let lookup_safe = encodeURI(lookup);
                return "https://nominatim.openstreetmap.org/search?street=" + lookup_safe + "&city=Glasgow&country=United+Kingdom&format=json&limit=5&polygon_geojson=1"
            },

            search_submit(event) {
                this.search(this.search_term);
            },

            search(term){
                let search_url = this.build_search_url(term);
                this.selected = null;
                axios.get(search_url).then(response => {
                    this.results = response.data;
                });
            },

            map_click(event) {
                console.log('map_click');
            },

            result_click(result) {
                this.selected = result;
                this.geojson = result.geojson;
                this.$refs.map.resize_to_fit();
                this.update_form(result.place_id);
            },

            update_form(id) {
                let record_input = document.getElementById('id_place_id');
                if (record_input){
                    record_input.value = id;
                }
            }
        }
    }
</script>