<template>
    <div>
        <h1>Thank you for participating!</h1>
        <p>Once the study is done all results will be released as creative commons.</p>
        <p>If you want to be notified when this happens you can follow me on twitter <a target="about:blank" href="https://twitter.com/oweissbarth">here</a>.</p>
        <hr/>
        <h2>You got {{correct}} out of {{total}} correct. That's {{correct/total*100}}%</h2>
        <table>
            <tr v-for="e in results" :key="e._id">
                <td class="type">{{e.type}}</td>
                <td><img class="preview" :src="'/api/images/'+e._id"/></td>
                <td>Title: {{e.title}}<br/>
                    Author: {{e.author}}<br/>
                    URL: <a target="_blank" :href="e.url">{{e.url}}</a>
                </td>
                <td v-if="e.correct=='correct'" class="correct">
                    You got this one right.
                </td>
                <td v-if="e.correct=='wrong'" class="wrong">
                    You got tricked by this one.
                </td>
                <td v-if="e.correct=='seen'">
                    You skipped this one.
                </td>
            </tr>
        </table>
    </div>
</template>
<script >
export default{
  props: {
    correct: 0,
    total: 0,
    results: {
      type: Array,
      default: () => []
    }
  }
}
</script>
<style >
    .preview{
        width: 100px;
    }
    tr{
        text-align: left;
    }
    td{
        border-bottom: 1px solid grey;
        padding: 1em;

    }
    table{
        border-collapse: collapse;
    }
    .type{
        font-weight: bold;
        font-size: 16pt;
    }
    .correct{
        color: green;
    }
    .wrong{
        color: red;
    }
</style>
