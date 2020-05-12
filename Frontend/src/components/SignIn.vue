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
                  <h2 class="dark-grey-text mb-5"><strong>Sign in</strong></h2>
                </div>
                <img
                  class="avatar"
                  src="@/assets/cattle.png"
                  alt="Portrait"
                />
                <mdb-input label="Your email" type="email" v-model="email" />
                <mdb-input
                  label="Your password"
                  type="password"
                  containerClass="mb-0"
                  v-model="password"
                />
                <div class="hint">
                  <!--Hint for wrong users' information -->
                  <p v-if="emailNotFound" class="font-small red-text d-flex">
                    Incorrect Email
                  </p>
                  <p
                    v-else-if="passwordUnmatched"
                    class="font-small red-text d-flex"
                  >
                    Incorrect Password
                  </p>
                </div>

                <!--Link for Forgetting Password -->
                <p class="font-small grey-text d-flex justify-content-end pb-3">
                  Forgot
                  <router-link to="/forgetpassword" class="blue-text ml-1"
                    >Password?</router-link
                  >
                </p>
                <div class="text-center mb-3">
                  <!--Button for Signin -->
                  <mdb-btn
                    type="button"
                    gradient="blue"
                    rounded
                    class="btn-block z-depth-1a signin-btn"
                    @click="authenticate"
                    >Sign in</mdb-btn
                  >
                </div>
              </mdb-card-body>
              <mdb-modal-footer class="mx-5 pt-3 mb-1 footer-signin">
                <!--Link for Signup -->
                <p class="font-small grey-text d-flex justify-content-end">
                  Not a member?
                  <router-link to="/signup" class="blue-text ml-1"
                    >Sign Up</router-link
                  >
                </p>
              </mdb-modal-footer>
            </mdb-card>
          </mdb-col>
        </mdb-row>
      </section>
    </mdb-col>
  </mdb-row>
</template>

<script>
import {
  mdbRow,
  mdbCol,
  mdbCard,
  mdbCardBody,
  mdbInput,
  mdbBtn,
  mdbModalFooter,
} from "mdbvue";
import backend from "@/services/backend.js";
import { mapActions } from "vuex";

export default {
  name: "SignInNew",
  components: {
    mdbRow,
    mdbCol,
    mdbCard,
    mdbCardBody,
    mdbInput,
    mdbBtn,
    mdbModalFooter,
  },
  data() {
    return {
      showModal: false,
      passwordUnmatched: false,
      emailNotFound: false,
      email: "w305475116@gmail.com",
      password: "123123",
    };
  },
  methods: {
    async authenticate() {
      const data = await backend.login(this.email, this.password);
      if (data === undefined) {
        alert("Something goes went in the server...");
      } else {
        try {
          const resp = data.data;
          console.log(resp);
          if (resp["code"] === 200) {
            var id = "all";
            var userData = resp["user"];
            localStorage.setItem("user", JSON.stringify(userData));
            this.login(userData).then(() =>
              this.$router.push({ path: `/home/${id}` })
            );
          } else {
            if (resp["code"] === 100) {
              this.passwordUnmatched = true;
            } else if (resp["code"] === 300) {
              this.emailNotFound = true;
            }
          }
        } catch {
          console.log("error");
        }
      }

      // ID 1000 means herds
    },
    ...mapActions({
      login: "login", // map `this.login()` to `this.$store.dispatch('login')`
    }),
  },
};
</script>

<style scoped>
.dairy-img {
  width: 110%;
  height: calc(100vh);
}

.cardbody {
  height: calc(100vh);
}

.avatar {
  width: 120px;
  height: 120px;
  margin-top: -20px;
}

.signin-btn {
  margin-top: 40px;
  margin-bottom: -10px;
}

.hint {
  margin-top: -10px;
  min-height: 30px;
  margin-bottom: -5px;
}

.footer-signin {
  margin-top: -60px;
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
