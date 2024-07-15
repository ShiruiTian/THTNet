"""
Created by tianshirui at 20240714 20:45
"""


from datasets import kitti, sampler, nuscenes_data


def get_dataset(config, type='train', **kwargs):
    if config.dataset == 'kitti':
        data = kitti.kittiDataset(path=config.path,
                                  split=kwargs.get('split', 'train'),
                                  category_name=config.category_name,
                                  coordinate_mode=config.coordinate_mode,
                                  preloading=config.preloading,
                                  preload_offset=config.preload_offset if type != 'test' else -1)
    elif config.dataset == 'nuscenes':
        data = nuscenes_data.NuScenesDataset(path=config.path,
                                             split=kwargs.get('split', 'train_track'),
                                             category_name=config.category_name,
                                             version=config.version,
                                             key_frame_only=True if type != 'test' else config.key_frame_only,
                                             # can only use keyframes for training
                                             preloading=config.preloading,
                                             preload_offset=config.preload_offset if type != 'test' else -1,
                                             min_points=1 if kwargs.get('split', 'train_track') in
                                                             [config.val_split, config.test_split] else -1)
    else:
        data = None

    if type == 'train_siamese':
        return sampler.PointTrackingSampler(dataset=data,
                                            random_sample=config.random_sample,
                                            sample_per_epoch=config.sample_per_epoch,
                                            config=config)
    elif type.lower() == 'train_motion':
        return sampler.MotionTrackingSampler(dataset=data,
                                             config=config)
    else:
        return sampler.TestTrackingSampler(dataset=data, config=config)
