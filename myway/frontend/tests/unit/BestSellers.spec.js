import { mount } from '@vue/test-utils'
import BestSellers from '@/components/BestSellers.vue'

// Mock image imports
jest.mock('@/assets/mercedes-logo.png', () => 'mock-mercedes.png')
jest.mock('@/assets/bmw-logo.png', () => 'mock-bmw.png')
jest.mock('@/assets/audi-logo.png', () => 'mock-audi.png')
jest.mock('@/assets/porsche-logo.png', () => 'mock-porsche.png')
jest.mock('@/assets/toyota-logo.png', () => 'mock-toyota.png')

describe('BestSellers.vue', () => {
  let wrapper

  beforeEach(() => {
    wrapper = mount(BestSellers)
  })

  test('renders the component with title', () => {
    expect(wrapper.find('h2').text()).toBe('Our Best Sellers')
  })

  test('displays all logo images', () => {
    const images = wrapper.findAll('img')
    expect(images).toHaveLength(5)
    
    expect(images[0].attributes('alt')).toBe('Logo 1')
    expect(images[1].attributes('alt')).toBe('Logo 2')
    expect(images[2].attributes('alt')).toBe('Logo 3')
    expect(images[3].attributes('alt')).toBe('Logo 4')
    expect(images[4].attributes('alt')).toBe('Logo 5')
  })

  test('applies correct CSS classes', () => {
    const container = wrapper.find('div.flex')
    expect(container.classes()).toContain('flex-wrap')
    expect(container.classes()).toContain('justify-center')
    
    const logoDiv = wrapper.find('div.flex-shrink-0')
    expect(logoDiv.classes()).toContain('w-24')
    expect(logoDiv.classes()).toContain('h-24')
  })

  test('renders responsive classes', () => {
    const logoDiv = wrapper.find('div.flex-shrink-0')
    expect(logoDiv.classes()).toContain('md:w-32')
    expect(logoDiv.classes()).toContain('md:h-32')
  })
})