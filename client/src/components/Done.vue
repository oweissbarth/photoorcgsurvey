<template>
    <div>
        <h1>Thank you for participating!</h1>
        <p>Once the study is done all results will be released as creative commons.</p>
        <p>If you want to be notified when this happens you can follow me on twitter <a target="about:blank" href="https://twitter.com/oweissbarth">here</a>.</p>
        <hr/>
        <h2>You got {{correct}} out of {{total}} correct. That's {{correct/total*100}}%</h2>
        <table>
            <tr v-for="e in results">
                <td>{{e.hash}}</td>
            </tr>
        </table>
    </div>
</template>
<script >
export default{
  props: {
    correct: 0,
    total: 0,
    results: []
  }
}
</script>
