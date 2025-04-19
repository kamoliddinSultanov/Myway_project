import { mount } from '@vue/test-utils'
import ImageCarousel from '@/components/ImageCarousel.vue'

jest.mock('@/assets/image1.jpg', () => 'mock-image1.jpg')
jest.mock('@/assets/image2.jpg', () => 'mock-image2.jpg')
jest.mock('@/assets/image3.jpg', () => 'mock-image3.jpg')

describe('ImageCarousel.vue', () => {
  let wrapper

  beforeEach(() => {
    wrapper = mount(ImageCarousel)
  })

  afterEach(() => {
    jest.clearAllTimers()
    wrapper.unmount()
  })

  test('render carousel of imgs', () => {
    expect(wrapper.find('.flex').exists()).toBe(true)
    expect(wrapper.findAll('.min-w-full')).toHaveLength(3)
  })

  test('displays the right active img', () => {
    expect(wrapper.vm.currentIndex).toBe(0)
    expect(wrapper.find('.flex').attributes('style')).toContain('translateX(-0%)')
  })

  test('goes to the next img via button', async () => {
    const nextBtn = wrapper.find('button:nth-of-type(2)')
    await nextBtn.trigger('click')
    expect(wrapper.vm.currentIndex).toBe(1)
    expect(wrapper.find('.flex').attributes('style')).toContain('translateX(-100%)')
  })

  test('goes to the previous img via button', async () => {
    wrapper.setData({ currentIndex: 1 })
    await wrapper.vm.$nextTick()
    
    const prevBtn = wrapper.find('button:nth-of-type(1)')
    await prevBtn.trigger('click')
    expect(wrapper.vm.currentIndex).toBe(0)
  })

  test('swithces imgs via indicators', async () => {
    const indicators = wrapper.findAll('.absolute.bottom-4 button')
    await indicators[2].trigger('click')
    expect(wrapper.vm.currentIndex).toBe(2)
  })

  test('auto slide', () => {
    jest.useFakeTimers()
    wrapper.vm.startAutoSlide()
    jest.advanceTimersByTime(3000)
    expect(wrapper.vm.currentIndex).toBe(1)
  })

  test('останавливает автопереключение при уничтожении', () => {
    jest.useFakeTimers()
    const clearIntervalSpy = jest.spyOn(global, 'clearInterval')
    wrapper.unmount()
    expect(clearIntervalSpy).toHaveBeenCalled()
  })

  test('корректно обрабатывает переход через границы', async () => {
    // Проверка перехода вперед на последнем слайде
    wrapper.setData({ currentIndex: 2 })
    await wrapper.vm.nextSlide()
    expect(wrapper.vm.currentIndex).toBe(0)

    // Проверка перехода назад на первом слайде
    wrapper.setData({ currentIndex: 0 })
    await wrapper.vm.prevSlide()
    expect(wrapper.vm.currentIndex).toBe(2)
  })
})