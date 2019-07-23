let url = 'http://127.0.0.1:8000/core/add_answer/'

function hello(){

alert('it works')

}

hello()


console.log("hello")

const answer = document.querySelector('#ans' );
const ansButton = document.querySelector('#answer-button');
const csrftoken = Cookies.get('csrftoken')


ansButton.addEventListener('click', (e) =>{
    console.log('Its working')
    fetch(url ,{
        credentials: 'include',
          method: 'POST',
          headers: {
            'X-CSRFToken': csrftoken
          },
          body: JSON.stringify({ 'body': ouranswername })
        })
    .then(data => data.json())
    .then(json => {
        console.log(json)
        const ansDiv=  document.querySelector('question_detail')
        answerDiv.innerHTML += `
        ${ json['user'] }:
        <p>
            ${json['body'] }
        </p>
        
    `
     })
    });