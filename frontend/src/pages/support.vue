<template>
<div class="support_wrap"> 
    <div class="overlay">
    </div>
    <div class="container">  
        <div class="left">
        <div class="left_content"> <li> Поддержка проектов<br> промышленной отрасли </li>
        <div class="container_image"><img src="../statics/image/dontknow.svg">
        </div>
        </div>
             <div class="left_content"> <li> Поддержка проектов малого и <br> среднего бизнеса </li>
        <div class="container_image"><img src="../statics/image/dontknow.svg">
        </div>
        </div>
             <div class="left_content"> <li> Поддержка проектов<br> аграрной отрасли </li>
        <div class="container_image"><img src="../statics/image/dontknow.svg">
        </div>
        </div>
             <div class="left_content"> <li> Поддержка<br>экспорта </li>
        <div class="container_image"><img src="../statics/image/dontknow.svg">
        </div>
        </div>
        </div>
        <div class="right">
            <h1 class = "title">Виды<br> государственной <br> поддержки </h1>
        </div>
    </div>
</div>
  </template>
<script>

</script>
<style scoped>
.left{
    border-right: 1px solid rgba(255, 255, 255, 0.6);
    width:50%;
    justify-content: flex-end;
    align-self: flex-end;
    display: flex;
    flex-direction: column;
}
.overlay{
    position: absolute;
    background:rgba(0, 0, 0, 0.6);
    height: 100vh;
    width:100%;
}
.right{
    display: flex;
    align-items: center;
    width:50%;
}
.title{
    font-size: 4.5vw;
    letter-spacing:0.01vw;
    font-weight: 600;
    margin-left:2%;
}
.support_wrap{
    
    display: flex;
    align-items: center;
    justify-content: center;
    background: url('../statics/image/Lipetsk_sup.png');
    background-size: cover;
    min-height:100vh;
}
.left_content{

    margin-top: 5%;
    margin-right: 5%;
    display: flex;
    justify-content: flex-end;
    align-items: center;
    text-align: right;
}
.container{
    display: flex;
    justify-content: center;
    z-index: 1;
    width: 100%;
    color:white;
    height: 100%;
}
.container li{
    cursor: pointer;
    font-size: 0.8vw;
    width:30%;
    list-style: none;
}
.container_image{
    margin-left: 5%;
    height:10vh;
}
.container_image img{
    height: 100%;
}
</style>