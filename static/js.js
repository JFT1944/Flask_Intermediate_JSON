// document.querySelector('body').style.background = 'black'
// $('body').css('background', 'red');

// const axios = require('axios');

async function getCupcakes(){

try{let gettingCupcakes = await axios.get('/api/cupcakes').then((res)=>{
    //console.log(res.data)
    for(let cc of res.data){
        //console.log(cc.cupcake.flavor)
        cc_wrapper = document.createElement('div')
        cc_image = document.createElement('img')
        //console.log(cc.cupcake.image)
        try{cc_image.setAttribute('src', cc.cupcake.image)
    }catch(e){
        //console.log(e)
    }
        let cc_info_wrapper = document.createElement('div')
        let cc_info = document.createElement('div')
        let cc_flavor = document.createElement('div')
        let cc_size = document.createElement('div')
        let cc_rating = document.createElement('div')
        cc_rating.innerText = cc.cupcake.rating
        cc_size.innerText = cc.cupcake.size
        cc_flavor.innerHTML = `<a href="/api/cupcakes/${cc.cupcake.id}">${cc.cupcake.flavor}</a>`
        cc_info.append(cc_flavor)
        cc_info.append(cc_size)
        cc_info.append(cc_rating)
        cc_info_wrapper.append(cc_info)
        cc_wrapper.append(cc_image)
        cc_wrapper.append(cc_info_wrapper)
        let hrr = document.createElement('hr')
        cc_wrapper.append(hrr)
        cc_wrapper.classList.add('cc_wrapper')
        document.getElementById('available_cupcakes').append(cc_wrapper)
        
    }
})
} catch(e){
    //console.log(e)
}

}
getCupcakes()


document.getElementById('add').addEventListener('click', ()=>{
    document.querySelector('#form_wrapper').style.display = 'flex'
})

async function addNewCupcake(newCC){
let NCC = await axios({
    method: 'post',
    url: '/api/cupcakes',
    data: {
      flavor: newCC.flavor.value,
      size: newCC.size.value, 
      rating: newCC.rating.value,
      image: newCC.image.value
}});
}


document.querySelector('#add_new_cc').addEventListener('submit', (e)=>{
    e.preventDefault()
    //console.log(e.target.flavor.value)
    //console.log(e.target.size.value)

    try {
    addNewCupcake(e.target).then((res)=>{
        //console.log(res)
        $('#form_wrapper').css('display', 'none')
    })
    } catch (e) {
    //console.log(e)
}
try {
    location.reload()
    // // $('#cc_wrapper').remove()
    // getCupcakes().then((res)=>{
    //     //console.log(res)
    // })
} catch (e) {
    
}
    
})

document.querySelector('#form_wrapper').addEventListener('click', (e)=>{
    e.preventDefault
    //console.log(e.target.id)
    if(e.target.id === 'form_wrapper'){
        $('#form_wrapper').css('display','none')
    }
})
