<template>
  <div class="about">
    <section id="content" class="content">
      <div class="thumb first-row">
        <div class="left">
          <div class="card">
            <div class="img"></div>
            <div class="avatar"></div>
            <div class="user-info">
              <h3 class="name">
                {{ name }}
              </h3>
              <p class="slogan">
                {{ slogan }}
              </p>
            </div>
          </div>
        </div>
        <div class="right">
          <div class="card"></div>
        </div>
      </div>
      <div class="whole second-row">
        <div class="card"></div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: "User",
  data() {
    return {
      name: "Tim",
      slogan: "I like the way you work it No diggity I wanna bag it up",
    };
  },
};
</script>

<style scoped>
#content {
  padding: 40px;
}

.thumb {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
}

.thumb .left {
  width: 38%;
}

.thumb .right {
  width: 60%;
}

.thumb .card {
  height: 600px;
  width: 100%;
  background: white;
  border-radius: 12px;
  margin-bottom: 2em;
}

.thumb .left .img {
  background: url("../assets/bg.png") no-repeat;
  background-size: cover;
  width: 100%;
  height: 30%;
  border-radius: 12px;
}

.thumb .left .user-info {
  width: 100%;
  height: 50%;
}

h3,
p {
  text-align: center;
}

p {
  width: 50%;
  margin: auto;
  margin-top: 40px;
  font-size: 18px;
  color: #66615b;
}

.thumb .left .avatar {
  background: url("../assets/logo.png") no-repeat;
  background-size: contain;
  width: 80px;
  height: 80px;
  border: 10px;
  box-shadow: 0px 10px 40px rgba(0, 0, 0, 0.2);
  border-radius: 50%;
  margin: auto;
}

.whole .card {
  height: 400px;
  width: 100%;
  background: white;
  border-radius: 12px;
  margin-bottom: 2em;
}
</style>
