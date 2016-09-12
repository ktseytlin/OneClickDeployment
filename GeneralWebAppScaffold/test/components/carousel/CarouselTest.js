import React from 'react';
import Carousel from '../../../components/carousel/Carousel.js';
import TestUtils from 'react-addons-test-utils';
import expect from 'expect';

describe('Carousel', () => {
  it('Should create a carousel of gifs', () => {
    const renderer = TestUtils.createRenderer();
    renderer.render(<Carousel />);
    result = renderer.getRenderOutput();
    expect(result.toEqual(<Carousel />));
  })
})
