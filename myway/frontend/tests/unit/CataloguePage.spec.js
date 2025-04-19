// tests/unit/CataloguePage.spec.js
import { mount } from '@vue/test-utils'
import CataloguePage from '@/components/CataloguePage.vue'
import axios from 'axios'
import { nextTick } from 'vue'

jest.mock('axios')

describe('CataloguePage.vue', () => {
  let wrapper
  const mockCars = [
    {
      id: 1,
      title: 'Test Car 1',
      brand: 'Toyota',
      model: 'Camry',
      description: 'Test description 1',
      price: '25000',
      image: '/media/cars/test1.jpg'
    }
  ]

  beforeEach(() => {
    axios.get.mockResolvedValue({ data: mockCars })
    wrapper = mount(CataloguePage, {
      global: {
        stubs: ['router-link']
      }
    })
  })

  afterEach(() => {
    jest.clearAllMocks()
  })

  test('renders component correctly', () => {
    expect(wrapper.find('h1').text()).toBe('Catalogue')
    expect(wrapper.find('input').exists()).toBe(true)
  })

  test('fetches cars on mount', async () => {
    expect(axios.get).toHaveBeenCalledWith('http://localhost:8000/api/cars/')
    await wrapper.vm.$nextTick()
    expect(wrapper.vm.cars).toEqual(mockCars)
  })

  

  test('handles search functionality', async () => {
    const searchInput = wrapper.find('input')
    await searchInput.setValue('test')
    await new Promise(resolve => setTimeout(resolve, 500))
    
    expect(axios.get).toHaveBeenCalledWith('http://localhost:8000/api/search/', {
      params: { q: 'test' }
    })
  })

  test('formats price according to locale', () => {
    const price = wrapper.vm.formatPrice('25000')
    expect(typeof price).toBe('string')
    expect(price).toMatch(/\d+/)
  })

  test('handles API errors gracefully', async () => {
    const consoleSpy = jest.spyOn(console, 'error').mockImplementation(() => {})
    axios.get.mockRejectedValue(new Error('Network Error'))
    
    await wrapper.vm.fetchCars()
    await wrapper.vm.$nextTick()
    
    expect(consoleSpy).toHaveBeenCalled()
    expect(wrapper.vm.cars).toEqual([])
    consoleSpy.mockRestore()
  })

  test('shows loading state', async () => {
    wrapper.setData({ loading: true })
    await nextTick()
    expect(wrapper.find('.animate-spin').exists()).toBe(true)
  })
})