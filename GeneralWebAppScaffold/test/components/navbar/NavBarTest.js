import React from 'react';
import NavBar from '../../../components/navbar/NavBar.js';
import TestUtils from 'react-addons-test-utils';
import expect from 'expect';

describe('NavBar', () => {
  it('Should create the navigation bar', () => {
    const renderer = TestUtils.createRenderer();
    renderer.render(<NavBar />);
    result = renderer.getRenderOutput();
    expect(result.toEqual(<NavBar />));
  })
})
