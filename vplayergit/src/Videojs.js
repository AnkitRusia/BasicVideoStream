import React from 'react';
import videojs from 'video.js'
export default class VideoPlayer extends React.Component {
  componentDidMount() {
    this.player = videojs(this.videoNode, this.props, function onPlayerReady() {
      console.log('Video.js Ready', this)
    });
  }
  componentWillUnmount() {
    if (this.player) {
      this.player.dispose()
    }
  }
  render() {
    return (
      <div> 
        <div data-vjs-player>
          <video ref={ node => this.videoNode = node } className="video-js"></video>
        </div>
      </div>
    )
  }
}