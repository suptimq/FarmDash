<template>
  <mdb-row>
    <mdb-col md="7">
      <img class="dairy-img" src="@/assets/dairyimg.png" />
    </mdb-col>

    <mdb-col md="5">
      <section class="form-elegant">
        <mdb-row>
          <mdb-col md="12">
            <mdb-card>
              <mdb-card-body class="mx-4 cardbody">
                <div class="text-center">
                  <h2 class="dark-grey-text mb-5"><strong>Sign up</strong></h2>
                </div>
                <img class="portrait" src="@/assets/cattle.png" />
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
                  <p
                    v-if="password !== passwordConfirmed"
                    class="font-small red-text d-flex"
                  >
                    Passwords don't match
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
      showModal: false,
      userExist: false,
      dbError: false,
      username: "",
      email: "",
      password: "",
      passwordConfirmed: "",
    };
  },
  methods: {
    async register() {
      var user = this.encapsulate();
      const data = await backend.register(user);
      if (data === undefined) {
        // Handle Exception
      } else {
        const resp = data.data;
        console.log(resp);
        if (resp["code"] === 200) {
          this.$router.push({ path: `/signin` });
        } else {
          if (resp["code"] === 100) {
            this.userExist = true;
          } else if (resp["code"] === 300) {
            this.dbError = true;
          }
        }
      }
    },
    encapsulate() {
      var user = {
        username: this.username,
        email: this.email,
        password: this.password,
      };
      return user;
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
  height: 570px;
}
.portrait {
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
  height: 570px;
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
