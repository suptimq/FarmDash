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
                  <h2 class="dark-grey-text mb-5">
                    <strong>Reset Password</strong>
                  </h2>
                </div>
                <img class="portrait" src="@/assets/cattle.png" />
                <mdb-input
                  label="Your email"
                  type="email"
                  placeholder="Ken@cornell.edu"
                  disabled
                />
                <mdb-input
                  label="Your password"
                  type="password"
                  containerClass="mb-0"
                />
                <mdb-input
                  label="Confirm your password"
                  type="password"
                  containerClass="mb-0"
                />

                <div class="text-center mb-3">
                  <!-- Button for Reset -->

                  <mdb-btn
                    type="button"
                    gradient="peach"
                    rounded
                    class="btn-block z-depth-1a reset-btn"
                    @click="resetpassword"
                    >Reset</mdb-btn
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
  name: "Reset",
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
  methods:{resetpassword() {
      this.$router.push({ path: '/signin' });
    },
  },
};
</script>

<style scoped>
.dairy-img {
  width: 110%;
  height: calc(100vh);
}

.portrait {
  width: 120px;
  height: 120px;
  margin-top: -20px;
}

.cardbody {
  height: calc(100vh);
}

.reset-btn {
  margin-top: 62px;
  margin-bottom: 40px;
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
