import React from 'react';
import NukaCarousel from 'nuka-carousel';

const styles = {
  container: {
    width: '50%',
    boxShadow: 'rgba(0, 0, 0, 0.298039) 5px 0px 10px 1px',
    zIndex: 5,
    display: 'block',
    marginLeft: 'auto',
    marginRight: 'auto',
  },
  carousel: {
    height: '90%',
  },
};

const Carousel = () => (
  <div style={styles.container}>
    <NukaCarousel style={styles.carousel} wrapAround>
      <img src="http://www.clicktorelease.com/code/gif/1.gif" role="presentation" />
      <img src="https://media.giphy.com/media/nROin1uGTYc6c/giphy.gif" role="presentation" />
      <img src="https://media.giphy.com/media/mnyMpAyg1fB9C/giphy.gif" role="presentation" />
    </NukaCarousel>
  </div>
);

export default Carousel;
