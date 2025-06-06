import { shallowMount } from '@vue/test-utils'
import LoginPage from '@/components/LoginPage.vue'
import { createStore } from 'vuex'
import { createRouter, createWebHistory } from 'vue-router'

describe('LoginPage.vue', () => {
  let actions
  let store
  let router

  beforeEach(() => {
    actions = {
      login: jest.fn(() => Promise.resolve(true))
    }

    store = createStore({
      actions
    })

    router = createRouter({
      history: createWebHistory(),
      routes: []
    })

    router.push = jest.fn()
  })

  const mountComponent = () =>
    shallowMount(LoginPage, {
      global: {
        plugins: [store, router]
      }
    })

  it('render login form', () => {
    const wrapper = mountComponent()

    expect(wrapper.find('h2').text()).toBe('Login')
    expect(wrapper.find('input[type="text"]').exists()).toBe(true)
    expect(wrapper.find('input[type="password"]').exists()).toBe(true)
  })

  it('send form and redirect if succeed', async () => {
    const wrapper = mountComponent()

    await wrapper.find('input[type="text"]').setValue('testuser')
    await wrapper.find('input[type="password"]').setValue('testpass')
    await wrapper.find('form').trigger('submit.prevent')

    expect(actions.login).toHaveBeenCalled()
    expect(actions.login.mock.calls[0][1]).toEqual({
      username: 'testuser',
      password: 'testpass'
    })

    expect(router.push).toHaveBeenCalledWith('/')
  })

  it('shows error if login failed', async () => {
    actions.login = jest.fn(() => Promise.resolve(false))
    store = createStore({ actions })

    const wrapper = shallowMount(LoginPage, {
      global: {
        plugins: [store, router]
      }
    })

    await wrapper.find('input[type="text"]').setValue('wronguser')
    await wrapper.find('input[type="password"]').setValue('wrongpass')
    await wrapper.find('form').trigger('submit.prevent')

    await wrapper.vm.$nextTick()

    expect(wrapper.text()).toContain('Invalid credentials')
  })
})
