<template>
  <div>
    <md-card>
      <md-card-header>
        <div>
          <md-chip>Aug'19</md-chip>
          <md-chip>Sep'19</md-chip>
          <md-chip class="md-accent" md-clickable>Oct'19</md-chip>
          <md-chip>All History</md-chip>
        </div>
        <p></p>
        <md-divider></md-divider>
        <p></p>
        <div class="md-title">Donations in your name, <strong>Mr Green</strong></div>
        <div class="md-subhead">Your activities resulted in <strong> {{ "£ " + total.toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",") }} </strong> of donations in <strong>Oct 2019</strong></div>
        <p></p>
      </md-card-header>
      
      <md-card-content>

        <md-table v-model="items" md-card>
          <md-table-row slot="md-table-row" slot-scope="{ item }">
            <md-table-cell md-label="Company Name" md-sort-by="companyName">
              {{ item.companyName }}
            </md-table-cell>
            <md-table-cell md-label="Amount" md-sort-by="name" md-numeric md-sorted md-sortable>
              <i class="md-caption">{{ (item.amount/total).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",") + "%"}} </i>
              &nbsp;&nbsp;&nbsp;
              <strong> {{"£ " + item.amount.toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",") }} </strong>
            </md-table-cell>
          </md-table-row>
        </md-table>

      </md-card-content>
    </md-card>
  </div>
</template>

<script>
import axios from 'axios';
import {cCompaniesData} from '../data';

export default {
  name: 'DonateFrom',

  data() { return {
    items: JSON.parse(cCompaniesData).data,
    total: null
  }},

  mounted () {
    axios
      .get('https://reqres.in/api/users?page=2')
      .then(response => {
          this.x_items = response.data.data
          this.total = this.items.reduce((a, b) => a + eval(b['amount']), 0)
          console.log(this.total)
          })
      .catch(e => {this.errors.push(e)})
  }

}
</script>