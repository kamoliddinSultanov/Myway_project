import { mount } from '@vue/test-utils'
import HomePage from '@/components/HomePage.vue'

jest.mock('@/assets/image1.jpg', () => 'test-image-1.jpg')
jest.mock('@/assets/image2.jpg', () => 'test-image-2.jpg')
jest.mock('@/assets/image3.jpg', () => 'test-image-3.jpg')

describe('HomePage.vue', () => {
  test('valid reder of header', () => {
    const wrapper = mount(HomePage)
    expect(wrapper.find('h1').text()).toBe('Welcome to MyWay')
  })
})