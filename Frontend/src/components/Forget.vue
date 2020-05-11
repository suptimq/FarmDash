<template>
  <mdb-row>
    <mdb-col md="7">
      <img class="dairy-img" src="@/assets/dairyimg.png" />
    </mdb-col>

    <mdb-col md="5">
      <section class="form-elegant forget-panel">
        <mdb-row>
          <mdb-col md="12">
            <mdb-card>
              <mdb-card-body class="mx-4 cardbody">
                <div class="text-center">
                  <h2 class="dark-grey-text mb-5">
                    <strong>Retrieve Password</strong>
                  </h2>
                </div>
                <img
                  class="portrait"
                  src="@/assets/cattle.png"
                  alt="Portrait"
                />

                <mdb-input label="Your email" type="email" />

                <mdb-row>
                  <mdb-col md="8">
                    <mdb-input
                      label="Verification Code"
                      type="password"
                      containerClass="mb-0"
                    />
                  </mdb-col>
                  <mdb-col md="4">
                    <!-- Button for Verification -->

                    <mdb-btn
                      size="sm"
                      type="button"
                      outline="warning"
                      rounded
                      class="btn-block z-depth-1a verify-btn"
                      ><strong>Verify</strong></mdb-btn
                    >
                  </mdb-col>
                </mdb-row>

                <p class="font-small grey-text d-flex justify-content-end pb-3">
                  Go back? <router-link to="/signin" class="blue-text ml-1">Sign in</router-link>
                </p>
                <div class="text-center mb-3">
                  <mdb-btn
                    type="button"
                    gradient="peach"
                    rounded
                    class="btn-block z-depth-1a submit-btn"
                    @click="submit"
                    >Submit</mdb-btn
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

export default {
  name: "ForgetNew",
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
    };
  },
  methods: {
    // Submit the verification code to reset the password
    submit() {
      this.$router.push({ path: '/resetpassword' });
    },
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

.forget-panel {
  max-height: 570px;
}

.portrait {
  width: 120px;
  height: 120px;
  margin-top: -20px;
}

.submit-btn {
  margin-top: 35px;
  margin-bottom: 49px;
}

.verify-btn {
  min-width: 95px;
  margin-top: 30px;
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

.form-elegant .z-depth-1-half,
.form-elegant .btn:hover {
  -webkit-box-shadow: 0 5px 11px 0 rgba(85, 182, 255, 0.28),
    0 4px 15px 0 rgba(36, 133, 255, 0.15);
  box-shadow: 0 5px 11px 0 rgba(85, 182, 255, 0.28),
    0 4px 15px 0 rgba(36, 133, 255, 0.15);
}
</style>
