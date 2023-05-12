
window.onload = ()=>{
    console.log("로딩되었음.")


}

async function handleSignup(){
    const email = document.getElementById("email").value
    const username = document.getElementById("username").value
    const password = document.getElementById("password").value
    console.log(email)
    console.log(username)
    console.log(password)

    const response = await fetch('http//127.0.0.1:8000/users/signup/', {
        headers:{
            'content-type': 'application/json',
        },
        method:'POST',
        body:{
            "email":email,
                "password":password,
            "username":username
        }
    })

    console.log(response)
}

