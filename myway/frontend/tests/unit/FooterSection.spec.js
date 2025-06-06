import { mount } from '@vue/test-utils'
import FooterSection from '@/components/FooterSection.vue'
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'Home' },
    { path: '/catalogue', name: 'Catalogue' },
    { path: '/about-us', name: 'About' },
  ]
})

describe('FooterSection.vue', () => {
  beforeAll(async () => {
    router.push('/')
    await router.isReady()
  })

  it('renders footer with navigation links and social icons', () => {
    const wrapper = mount(FooterSection, {
      global: {
        plugins: [router],
      },
    })

    expect(wrapper.text()).toContain('Home')
    expect(wrapper.text()).toContain('Car Catalogue')
    expect(wrapper.text()).toContain('About Us')

    const links = wrapper.findAll('a')
    expect(links.length).toBeGreaterThanOrEqual(6)

    expect(wrapper.text()).toContain('© 2025 Company Ltd. All rights reservered.')
  })
})
