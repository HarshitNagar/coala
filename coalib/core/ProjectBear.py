from coalib.core.Bear import Bear
from coalib.settings.FunctionMetadata import FunctionMetadata


class ProjectBear(Bear):
    """
    This bear base class does not parallelize tasks at all, it runs on the
    whole file base provided.
    """

    def __init__(self, section, file_dict, cache=None):
        """
        :param section:
            The section object where bear settings are contained. A section
            passed here is considered to be immutable.
        :param file_dict:
            A dictionary containing filenames to process as keys and their
            contents (line-split with trailing return characters) as values.
        :param cache:
            A cache the bear can use to speed up runs. If ``None``, no cache
            will be used.
        """
        Bear.__init__(self, section, file_dict, cache)

        self._kwargs = self.get_metadata().create_params_from_section(section)

    @classmethod
    def get_metadata(cls):
        """
        :return:
            Metadata for the ``analyze`` function extracted from its signature.
            Excludes parameters ``self`` and ``files``.
        """
        return FunctionMetadata.from_function(
            cls.analyze,
            omit={'self', 'files'})

    def generate_tasks(self):
        return ((self.file_dict,), self._kwargs),
