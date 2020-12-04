var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function()
    {
        var productId = this.dataset.product 
        var action = this.dataset.action
        console.log('productId:', productId, 'action:', action )
        console.log("User:", user)
        if (user == 'AnonymousUser'){
            
            console.log("user is not logged in.")
        }else{
            // console.log("user is logged in.")
            updateUserOrder(productId, action)
        }
    }
    )
}

function updateUserOrder(productId, action){
    var url = '/updateitem'
    fetch(url, {
        method:'POST',
        headers:{
            'content-type':'application/json',
            'x-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productID':productId, 'action':action})
    })

    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        console.log('date', data)
        location.reload()
    })
}