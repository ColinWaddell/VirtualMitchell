
<template>
  <div class="map">
    <div style="height: 450px">
        <vuemap :clickhandler="load_place" :geojson="geojson"></vuemap>
    </div>
    <div v-if="records">
        <h6 class="text-secondary">{{ records.length }} Record<span v-if="records.length > 1">s</span> found:</h6>
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
                    <!-- {{ record.record_number }} -->
                    <td width="250" style="
                        background: white;
                        padding: 10px;
                        margin: 0;
                    ">
                        <div class="record-thumbnail">
                            <a 
                                v-if="superuser" 
                                class="badge badge-pill badge-secondary record-control"
                                :href="editurl + record.id">
                                    <span class="glyphicon glyphicon-edit" aria-hidden="true"></span>
                            </a>
                            <a 
                                v-else
                                class="badge badge-pill badge-secondary record-control"
                                :href="reporturl + record.id + returnurl">
                                    <span class="glyphicon glyphicon-exclamation-sign" aria-hidden="true"></span>
                            </a>

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
        <p hidden class="text-muted font-italic">{{ place_id }}</p>
    </div>
    <div v-else class="alert alert-info" role="alert">
        Select something from the map
    </div>
  </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: 'vmmapsearch',

        data () {
            console.log(this.$router) 
            return {
                records: null,
                display_name: null,
                geojson: locations,
                superuser: false,
                place_id: null,
                baseurl: "http://www.mitchelllibrary.org/virtualmitchell/",
                editurl: "/record/edit/",
                reporturl: "/record/report/",
                returnurl: `/?return=${ encodeURIComponent(window.location.pathname) }${ encodeURIComponent(window.location.search) }`
            }
        },

        mounted() {
            if(window.superuser){
                this.superuser = true;
            }
            window.setTimeout(() => {
                if (this.geojson.length == 1){
                    this.load_records_url(this.geojson[0].properties.record_request_url);
                }
            }, 0);
        },

        methods: {
            load_place: function (event) {
                let records_url = event.layer.feature.properties.record_request_url;
                let display_name = event.layer.feature.properties.display_name;
                this.place_id = event.layer.feature.properties.place_id;

                this.load_records_url(records_url, display_name);
                // this.jump_to_spot(event.latlng); // needs work
            },

            load_records_url: function(records_url, display_name) {
                axios.get(records_url).then(response => {
                    this.records = response.data;
                    this.display_name = display_name
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