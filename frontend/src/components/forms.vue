<template>
<div>        
     <q-btn-dropdown  dropdown-icon="chat"
     outline round color="white"
    :content-style="{ backgroundColor: 'rgba(0, 0, 0, 0)' }"
    :glossy=true
    
    :dense=true
 class="absolute"
>
  <div class="wrapp">
         <q-btn outline round color="white" icon="assignment" size='1.5vh' class="one" @click="show=!show">
                 <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">
          <strong>Мы с вами свяжемся</strong>
          (<q-icon name="keyboard_arrow_left"/>)
        </q-tooltip>
         </q-btn>
    <q-btn outline round color="white" icon="call" size='1.5vh' class="one"/>
</div>
</q-btn-dropdown>
     <q-form
      @submit="onSubmit"
      @reset="onReset"
      class="fixed-center"
      v-if="show"
    >

    <div class="form_button">
    <q-btn 
    :dense=true
    flat round color="white" icon="close" @click="show=!show"/>
    </div>
    <div class="form_container">
          <h2 class="left-top">
      Связаться с нами
    </h2>
   
        <q-input
        dark outlined
        v-model="surname"
        label-color = 'grey-2'
        class="input"
        
        label="Ваша фамилия *"
        lazy-rules
        :rules="[ val => val && val.length > 0 || 'Пожалуйста, введите вашу фамилию']"
      />
      <q-input
        dark outlined
        v-model="name"
        class="input"
        label-color = 'grey-2'
        label="Ваше имя *"
        lazy-rules
        :rules="[ val => val && val.length > 0 || 'Пожалуйста, введите имя']"
      />
  
            <q-input
      
        dark outlined
        class="input"
        label-color = 'grey-2'
        v-model="middle_name"
        label="Ваше отчество *"
        lazy-rules
        :rules="[ val => val && val.length > 0 || 'Пожалуйста, введите ваше отчество(если есть)']"
      />
            <q-input
            dark outlined
        class="input"
        label-color = 'grey-2'
        type = 'number'
        v-model="phone"
        label="Телефон *"
        lazy-rules
        :rules="[ val => val && val.length > 0 || 'Пожалуйста, введите свой номер телефона']"
      />
      <q-input
      class="input"
        dark outlined
        :readonly="readonly"
        type='email'
        v-model="email"
        label="Почта*"
        lazy-rules
        :rules="[ val => val && val.length > 0 || 'Пожалуйста, введите вашу почту']"
      />
            <q-input
        class="bottom"
        label-color = 'grey-2'
       dark outlined
        v-model="organisation"
        label="Организация*"
      />
      <div>
        <q-btn label="Отправить" type="submit" color="primary"/>
        <q-btn label="Сбросить" type="reset" color="primary" flat class="q-ml-sm" />
      </div>
        </div>
    </q-form>
</div>
</template>
<script>
export default {
    data(){
        return{
      show:false,
      name:null,
      phone:null,
      middle_name:null,
      organisation:null,
      leftDrawerOpen: false,
      info:null,
      surname:null,
      email:null,
        }
    },
     methods: {
      onReset () {
    this.name = null
    this.middle_name = null
    this.organisation = null
    this.phone = null
    this.surname = null
    this.email = null
     },
    onSubmit () {
      let data2 ={name:this.name,
                  surname:this.surname,
                  middle_name:this.middle_name,
                  email:this.email,
                  organisation:this.organisation,
                  phone:this.phone
                  }
      let data = JSON.stringify(data2)
    fetch('http://127.0.0.1:8000/',{
      method:'POST',
      body:data,
      headers:{'content-type':'application/json'}
    }).then(function(response){
      return response.json()
    }).then(function(data){
      alert('С вами свяжутся')
    })
    this.onReset()
    data.show=!show
    },

  }
}
</script>
<style scoped>
.absolute{
  right: 0;
  margin-right: 2%;
  margin-top: 43%;
  z-index: 10;
}
.left-top{
  padding-bottom: 5%;
  margin: 0;
  color:white;
  font-size: 2.3vw;
}

.flex{
  align-items: center;
  justify-content: space-between;
}
.input{
  opacity: .5;
  width:80%;
  margin:0 auto;
}
.wrapp{
  align-items: center;
  display: flex;
  flex-direction: column;
}
.form_container{
  width:95%;
  margin: 0 auto;
}
.bottom{
  width:80%;
  margin:0 auto;
  margin-bottom: 10%;
}
.one{ 
  margin-bottom: 10%;

}
.fixed-center{
  z-index: 10;
  display:flex;
  flex-direction: column;
  height:73%;
  width: 40%;
  background:rgba(0, 0, 0,.7);
}


.form_button{
  position: absolute;
  top:0;
  right:2%;
  justify-content: flex-end;
  align-items: flex-end;
}

</style>