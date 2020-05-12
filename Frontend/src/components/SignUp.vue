<template>
  <mdb-row class="frame">
    <mdb-col md="7">
      <img class="dairy-img" src="@/assets/dairyimg.png" />
    </mdb-col>

    <mdb-col>
      <section class="form-elegant">
        <mdb-row>
          <mdb-col md="12">
            <mdb-card>
              <mdb-card-body class="mx-4 cardbody">
                <div class="text-center">
                  <h2 class="dark-grey-text mb-5"><strong>Sign up</strong></h2>
                </div>
                <img class="avatar" src="@/assets/cattle.png" />
                <mdb-input label="Username" v-model="username" required />
                <mdb-input
                  label="Email"
                  v-model="email"
                  type="email"
                  required
                />
                <mdb-input
                  label="Password"
                  type="password"
                  containerClass="mb-0"
                  v-model="password"
                  required
                />
                <mdb-input
                  label="Confirm Password"
                  type="password"
                  containerClass="mb-0"
                  v-model="passwordConfirmed"
                  required
                />
                <div class="hint">
                  <!--Hint for unmatched passwords-->
                  <p class="font-small red-text d-flex">
                    {{ hinttext }}
                  </p>
                </div>

                <!-- Link for Signin -->
                <p class="font-small grey-text d-flex justify-content-end">
                  Have an account?
                  <router-link to="/signin" class="blue-text ml-1"
                    >Sign in</router-link
                  >
                </p>
                <div class="text-center mb-3">
                  <!-- Button for Signin -->
                  <mdb-btn
                    type="button"
                    color="default"
                    rounded
                    class="btn-block z-depth-1a signup-btn"
                    @click="register"
                    >Sign up</mdb-btn
                  >
                </div>
              </mdb-card-body>
            </mdb-card>
          </mdb-col>
        </mdb-row>
      </section>
    </mdb-col>
  </mdb-row>
</template>

<script>
import { mdbRow, mdbCol, mdbCard, mdbCardBody, mdbInput, mdbBtn } from "mdbvue";
import backend from "@/services/backend.js";

var hint0 = "Please fill in all the required fields!";
var hint1 = "Incorrect email format!";
var hint2 = "Passwords don't match!";
var hint3 = "The length of password should be at least 6 bits!";
var hint100 = "User has existed!";
var hint200 = "Successful!";
var hint300 = "The system is under maintenance! Please try again later.";

export default {
  name: "SignUpNew",
  components: {
    mdbRow,
    mdbCol,
    mdbCard,
    mdbCardBody,
    mdbInput,
    mdbBtn,
  },
  data() {
    return {
      //showModal: false,
      //userExist: false,
      //dbError: false,
      username: "",
      email: "",
      password: "",
      passwordConfirmed: "",
      hinttext: "",
    };
  },
  methods: {
    async register() {
      this.hinttext = "";
      if (
        this.email === "" ||
        this.username === "" ||
        this.password === "" ||
        this.passwordConfirmed === ""
      ) {
        this.hinttext = hint0;
        return;
      }
      if (!this.checkEmail()) {
        this.hinttext = hint1;
        // console.log("s");
        return;
      }
      // console.log("s");
      if (!this.checkPassword()) {
        this.hinttext = hint2;
        return;
      }
      if (this.password.length < 6) {
        this.hinttext = hint3;
        return;
      }
      let user = this.encapsulate();
      const data = await backend.register(user);
      if (data === undefined) {
        // Handle Exception
      } else {
        const resp = data.data;
        console.log(resp);
        if (resp["code"] === 200) {
          this.hinttext = hint200;
          this.$router.push({ path: `/signin` });
        } else {
          if (resp["code"] === 100) {
            //this.userExist = true;
            this.hinttext = hint100;
          } else if (resp["code"] === 300) {
            //this.dbError = true;
            this.hinttext = hint300;
          }
        }
      }
    },
    checkPassword() {
      return this.password === this.passwordConfirmed;
    },
    checkEmail() {
      let reg = /^([A-Za-z0-9_\-.])+@([A-Za-z0-9_\-.])+\.([A-Za-z]{2,4})$/;
      return reg.test(this.email);
    },
    encapsulate() {
      return {
        username: this.username,
        email: this.email,
        password: this.password,
      };
    },
    reset() {
      this.username = "";
      this.email = "";
      this.password = "";
      this.passwordConfirmed = "";
    },
  },
};
</script>

<style scoped>
.dairy-img {
  width: 110%;
  height: calc(100vh);
}

.avatar {
  width: 120px;
  height: 120px;
  margin-top: -20px;
}

.hint {
  margin-top: -10px;
  min-height: 30px;
  margin-bottom: -5px;
}

.signup-btn {
  margin-top: 29px;
  margin-bottom: 15px;
}

.cardbody {
  height: calc(100vh);
}

.form-elegant .font-small {
  font-size: 0.8rem;
}

.form-elegant .z-depth-1a {
  -webkit-box-shadow: 0 2px 5px 0 rgba(55, 161, 255, 0.26),
    0 4px 12px 0 rgba(121, 155, 254, 0.25);
  box-shadow: 0 2px 5px 0 rgba(55, 161, 255, 0.26),
    0 4px 12px 0 rgba(121, 155, 254, 0.25);
}

.form-elegant,
.form-elegant:hover {
  -webkit-box-shadow: 0 5px 11px 0 rgba(85, 182, 255, 0.28),
    0 4px 15px 0 rgba(36, 133, 255, 0.15);
  box-shadow: 0 5px 11px 0 rgba(85, 182, 255, 0.28),
    0 4px 15px 0 rgba(36, 133, 255, 0.15);
}
</style>
