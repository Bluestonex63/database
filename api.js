import {
	json,
	opine,
	urlencoded,
  } from "https://deno.land/x/opine@2.3.3/mod.ts";
const app = opine();
app.post('/', (req, res) => {

});

app.listen(3000);
console.log("Running!")