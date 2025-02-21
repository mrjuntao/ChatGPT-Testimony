function runPrompt( systemprompt = "", prompt = "Hello!", returnUsage = true, temperature = 0.7, maxLength = 256, topP = 1, frequencyPenalty = 0, presencePenalty = 0) {
 //initialize the return array
 var contents = [];
 //use your API Key here
 const apiKey = 'XXXXXX';
 //change the API URL here if you want to use a different API
 const url = 'https://api.openai.com/v1/chat/completions';
 //change the model here
 const model = 'gpt-4-turbo-2024-04-09';

 //request along with the parameters
 const request = {
  model: model,
  messages: [
    {
      "role": "system",
      "content": systemprompt
    },
    //add more user nodes for few shot prompts, function signature will need to change
    {
      "role": "user",
      "content": prompt
    }
  ],
  temperature: temperature,
  max_tokens: maxLength,
  top_p: topP,
  frequency_penalty: frequencyPenalty,
  presence_penalty: presencePenalty,
 };


 //headers
 const data = {
   contentType: "application/json",
   headers: { Authorization: "Bearer "+ apiKey },
   payload: JSON.stringify(request),
 };


 //connect to the OpenAI API, sending the headers and parse the JSON response
 const response = JSON.parse(UrlFetchApp.fetch(url, data).getContentText());


 //add the response message to the return array
 contents.push( response.choices[0].message.content );


 if ( returnUsage ) {
   //if the return usage is enabled, return the promtp_tokens and completion_tokens as well
   contents.push(response.usage.prompt_tokens);
   contents.push(response.usage.completion_tokens);
 }

 return contents;
}
